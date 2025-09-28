# testing-framework

## Como executar

Para que as importações entre os módulos do projeto funcionem corretamente, os arquivos devem ser executados como módulos do pacote, utilizando a opção `-m` do Python.

Por exemplo:

```bash
python3 -m examples.my_test
python3 -m tests.test_test_case
python3 -m tests.test_test_suite
```

> Não execute os arquivos diretamente, como:
> ```bash
> python3 examples/my_test.py
> ```
> Isso resultará em erros de importação (ModuleNotFoundError) porque o Python não reconhecerá a estrutura de pacotes do projeto.
