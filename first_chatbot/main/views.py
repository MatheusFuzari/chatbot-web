
from rest_framework.views import APIView
from rest_framework.response import Response
from bardapi import BardCookies
import requests
import json

psid = "g.a000gAjNcUuuip87AsR1wWkM3-EBUNy75LGVPk1grE8GQpif7bXW-HYlRUX3CjOQGGvP9Q-GMgACgYKAUMSAQASFQHGX2Mixjb478dr1r0ydfPsMWEOzhoVAUF8yKrslmg6z8SYUjhXmWbeAbP70076"
psidts = "sidts-CjIBPVxjSmC6PZaS2X0VI_3zMU22r-6gTs8gX_sKTR1iiuPD5BL0pp2QfD8VCqozr7q7TxAA"
psidcc = "ABTWhQG4LgJTcAYYAOJTeN6jw3cYYQtVYVaylEkgb4GwLyc3zpgjH7Ts4FXdcWz8QKDHIAp-"
#cria um conjunto com os tokens de autenticação
#para poder usar o Bard
tokenCookies = {
    "__Secure-1PSID": psid,
    "__Secure-1PSIDTS": psidts,
    "__Secure-1PSIDCC": psidcc, 
}
#cria o objeto bard para ser usado

mockedResponde = '{"content": "vai tomar no cu!"}'
enableMock = True

#define as ações da API para receber
#os comandos a ser passado para o Bard
class ChatBotAPIView(APIView):
    def post(self, request):
        bard = None
        answer = json.loads(mockedResponde)
        if enableMock == False:
            bard = BardCookies(cookie_dict=tokenCookies)
            answer = bard.get_answer(data['question'])
        
        #pega os dados que veio na requisição
        data = request.data

        #pega o dados da conversationId caso ele seja informado para mander a mesma conversa com o chatbot
        conversationId = data.get("conversationId")

        #verifica se o id da conversa foi recebido
        if(conversationId is not None):

            #informa o bard para responder na conversa desejada
            bard.conversation_id = conversationId
        elif enableMock == False:
            bard.conversation_id = None
        print(answer)
        return Response(status=201,data=answer)
