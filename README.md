## instalação das dependências
# pyenv
curl https://pyenv.run | bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

# poetry
curl -sSL https://install.python-poetry.org | python3 -
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

## configuração do projeto

# instalação python 3.10
pyenv install 3.10

# iniciar o ambiente virtual
pyenv local 3.10

# iniciar o poetry com a versão do pyenv
poetry env use $(pyenv which python)

# entrar no shell com o poetry
poetry shell

# instalar as dependências
poetry install

# iniciar a aplicação
python main.py
