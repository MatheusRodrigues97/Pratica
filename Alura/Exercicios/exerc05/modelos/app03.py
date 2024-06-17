class ContaBancaria:

    def __init__(self, titular, saldo):
        
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
        

    def __str__(self) -> str:
        return f' Titular da conta: {self._titular} \n Saldo {self._saldo}'
    
    @property
    def ativar_conta(self):
        self._ativo = not self._ativo