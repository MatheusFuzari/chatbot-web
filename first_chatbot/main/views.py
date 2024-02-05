
from rest_framework.views import APIView
from rest_framework.response import Response
from bardapi import BardCookies
import requests

psid = "g.a000gAjNca01zuClg2bbmXXAj_CMz0koyJvIgD3nhuz8mH1aQuS-H3ZgGCDPi4skP1-nxaXOfQACgYKAa4SAQASFQHGX2MiTc9oESkjk_jhUZn49evWwhoVAUF8yKrrAoDr3QzYZjAdc2NXLdRj0076"
psidts = "sidts-CjEBPVxjSlRIPBgis6-fIbv20V1_8Y1u9GpQSLkIW0STy95a8J5IeojGT7Rv4-pcF6cwEAA"
psidcc = "ABTWhQHF4baYSN1HR1Obi_ALTVD4_wIzjatMX91IzZC6gawCwkA3BdzOH5lvcJB7rwJ_0dBY5A"
#cria um conjunto com os tokens de autenticação
#para poder usar o Bard
tokenCookies = {
    "__Secure-1PSID": psid,
    "__Secure-1PSIDTS": psidts,
    "__Secure-1PSIDCC": psidcc, 
}
#cria o objeto bard para ser usado
bard = BardCookies(cookie_dict=tokenCookies)

#define as ações da API para receber
#os comandos a ser passado para o Bard
class ChatBotAPIView(APIView):
    def post(self, request):
        #pega os dados que veio na requisição
        data = request.data

        #pega o dados da conversationId caso ele seja informado para mander a mesma conversa com o chatbot
        conversationId = data.get("conversationId")

        #verifica se o id da conversa foi recebido
        if(conversationId is not None):

            #informa o bard para responder na conversa desejada
            bard.conversation_id = conversationId
        else:
            bard.conversation_id = None
        
        answer = bard.get_answer(data['question'])

        return Response(status=201,data=answer)

