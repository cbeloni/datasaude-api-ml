import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

from api.previsao_temporal.previsao_temporal_repository import get_previsao_temporal_historico_not_null_repository, upsert_paciente_previsao_by_data_repository, clean_paciente_previsao_after_data_repository, delete_unnecessary_paciente_previsao_after_data_repository
from api.previsao_temporal.schemas.previsao_temporal_schema import PacientePrevisaoSchema

def gera_csv_paciente_previsao_temporal(pacientes_previsoes) -> PacientePrevisaoSchema:
    nome_arquivo = 'dados_treino.csv'
    with open(nome_arquivo, 'w') as file:
        file.truncate(0)
        file.write("DT_ATENDIMENTO|ATENDIMENTOS" + '\n')
        for paciente_previsao in pacientes_previsoes:
            paciente_previsao = PacientePrevisaoSchema(**paciente_previsao)
            file.write(f"{paciente_previsao.data}|{paciente_previsao.valor_historico}" + '\n')
        

async def load_df(paciente_previsao: PacientePrevisaoSchema):
    pacientes_previsoes = await get_previsao_temporal_historico_not_null_repository(paciente_previsao)
    gera_csv_paciente_previsao_temporal(pacientes_previsoes)
    df = pd.read_csv('dados_treino.csv', sep='|')
    return df

async def treinar_modelo(qtd_dias_previsao: int, qtd_dias_sazonalidade: int, cid: str): 
    paciente_previsao = PacientePrevisaoSchema(cid=cid)
    df = await load_df(paciente_previsao)
    # print(df.head().to_dict(orient='records'))
    df['DT_ATENDIMENTO'] = pd.to_datetime(df['DT_ATENDIMENTO'])
    df.set_index('DT_ATENDIMENTO', inplace=True)
    ts = df['ATENDIMENTOS']
    model = ExponentialSmoothing(ts, trend='add', seasonal='add', seasonal_periods=qtd_dias_sazonalidade).fit()
    forecast = model.forecast(steps=qtd_dias_previsao)
    forecast_df = pd.DataFrame({
        'data': forecast.index.strftime('%Y-%m-%d'),
        'valor_previsao': forecast.values
    })
    result = []
    paciente_previsao = None
    for forecast_dt in forecast_df.iterrows():
        try:
            data = forecast_dt[1]['data']
            valor_previsao = int(forecast_dt[1]['valor_previsao'])
            paciente_previsao = PacientePrevisaoSchema(data=data, valor_previsao=valor_previsao)
            await upsert_paciente_previsao_by_data_repository(paciente_previsao)
            result.append(paciente_previsao)
        except:
            continue
    if (paciente_previsao is not None):
        await clean_paciente_previsao_after_data_repository(paciente_previsao)
        await delete_unnecessary_paciente_previsao_after_data_repository(paciente_previsao)
    return result