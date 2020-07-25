

import sys

from pyboleto.bank.bancodobrasil import BoletoBB
from pyboleto.bank.bradesco import BoletoBradesco
from pyboleto.bank.caixa import BoletoCaixa
from pyboleto.bank.itau import BoletoItau
from pyboleto.bank.santander import BoletoSantander
from pyboleto.html import BoletoHTML
from pyboleto.pdf import BoletoPDF
import datetime


def print_boleto_html(uuid):
    d = BoletoBradesco()
    d.carteira = '06'  # Contrato firmado com o Banco Bradesco
    d.cedente = 'Empresa ACME LTDA'
    d.cedente_documento = "102.323.777-01"
    d.cedente_endereco = "Rua Acme, 123 - Centro - Sao Paulo/SP - \
        CEP: 12345-678"
    d.agencia_cedente = '0278-0'
    d.conta_cedente = '43905-3'

    d.data_vencimento = datetime.date(2011, 1, 25)
    d.data_documento = datetime.date(2010, 2, 12)
    d.data_processamento = datetime.date(2010, 2, 12)

    d.instrucoes = [
        "- Linha 1",
        "- Sr Caixa, cobrar multa de 2% após o vencimento",
        "- Receber até 10 dias após o vencimento",
    ]
    d.demonstrativo = [
        "- Serviço Teste R$ 5,00",
        "- Total R$ 5,00",
    ]
    d.valor_documento = 2158.41

    d.nosso_numero = "1112011668"
    d.numero_documento = "1112011668"
    d.sacado = [
        "Cliente Teste %s" % uuid,
        "Rua Desconhecida, 00/0000 - Não Sei - Cidade - \
            Cep. 00000-000",
        ""
    ]

    boleto_HTML = BoletoHTML('boleto/' + uuid + '.html')
    boleto_HTML.drawBoleto(d)
    boleto_HTML.save()


def print_boleto_pdf(uuid):
    d = BoletoBradesco()
    d.carteira = '06'  # Contrato firmado com o Banco Bradesco
    d.cedente = 'Empresa ACME LTDA'
    d.cedente_documento = "102.323.777-01"
    d.cedente_endereco = "Rua Acme, 123 - Centro - Sao Paulo/SP - \
        CEP: 12345-678"
    d.agencia_cedente = '0278-0'
    d.conta_cedente = '43905-3'

    d.data_vencimento = datetime.date(2011, 1, 25)
    d.data_documento = datetime.date(2010, 2, 12)
    d.data_processamento = datetime.date(2010, 2, 12)

    d.instrucoes = [
        "- Linha 1",
        "- Sr Caixa, cobrar multa de 2% após o vencimento",
        "- Receber até 10 dias após o vencimento",
    ]
    d.demonstrativo = [
        "- Serviço Teste R$ 5,00",
        "- Total R$ 5,00",
    ]
    d.valor_documento = 2158.41

    d.nosso_numero = "1112011668"
    d.numero_documento = "1112011668"
    d.sacado = [
        "Cliente Teste %s" % uuid,
        "Rua Desconhecida, 00/0000 - Não Sei - Cidade - \
            Cep. 00000-000",
        ""
    ]
    boleto_PDF = BoletoPDF('boleto/' + uuid + '.pdf')
    boleto_PDF.drawBoleto(d)
    boleto_PDF.save()
