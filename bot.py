import os
import json
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot 



class Bot:

	dir_path = os.getcwd()

	def __init__(self, nome_bot):
		print(self.dir_path)
		self.bot = ChatBot(nome_bot)
		self.trainer = ListTrainer(self.bot)
		

	def mensagem(self, data):
		self.data = data
		print('data recebida=',self.data)
		mensagem = self.data.get('message')
		resposta = self.responde(mensagem)
		return resposta

	def responde(self, mensagem):
		resposta = self.bot.get_response(mensagem)
		resposta = str(resposta)
		resposta = self.create_dict(resposta)
		return resposta

	def create_dict(self, mensagem):
		self.mensagem = mensagem
		self.dict = {'name': 'Eva', 'message': ''}
		self.dict['message'] = self.mensagem
		return self.dict


	def treina(self,nome_pasta):
		conversa = ['Oi', 'Olá', 'Tudo bem?', 'sim e com você?', 'Eu estou bem', 'tambem vou bem']
		conversa2 = ['Bom Dia como você está?', 'Eu estou bem, e você?', 'Eu também estou', 'Que bom', 'Sim', 'Olá', 'Oi', 'Como vai você?', 'Eu estou bem', 'Que bom']
		conversa3 = ['Posso ajudá-lo com alguma coisa?', 'Sim, eu tenho uma pergunta', 'Qual é a sua pergunta?', 'Eu poderia pedir uma xícara de açúcar?', 'Me desculpe, mas eu não tenho nenhuma', 'Obrigado de qualquer maneira', 'Sem problemas']
		conversa4 = ['Como vai você?', 'Eu estou bem, e você?', 'Eu também estou bem', 'Isso é bom', 'Ouviu as notícias?', 'Que notícia?']
		conversa5 = ['Qual é o seu livro favorito?', 'Eu não sei ler', 'Então, qual é a sua cor favorita?', 'Azul', 'Quem é você?', 'Quem? Quem é senão uma forma seguindo a função de quê', 'Então o que você é?', 'Um homem em uma máscara', 'Eu posso ver isso?', 'Era uma piada kkkkk']
		conversa6 = ['você gosta de música?', 'Eu gosto de ver filmes', 'Que tipo de filme você gosta?', 'Alice no Pais das Maravilhas', 'Eu gostaria de ser o Chapeleiro Maluco', 'Você é totalmente maluco. Mas eu vou te contar um segredo. Todas as melhores pessoas são']
		conversa7 = ['Eu estou trabalhando em um projeto', 'Em que você está trabalhando?', 'Eu estou fazendo um bolo', 'O bolo é uma mentira', 'Não, não é. O bolo é delicioso', 'O que mais é delicioso?', 'Nenhuma coisa']
		conversa8 = ['Fale-me sobre você', 'O que você quer saber?', 'Você é um robô?', 'Sim eu sou', 'Como é?', 'O que mais que você quer saber?', 'Como você trabalha?', 'É complicado', 'Complexo é melhor que complicado','Simples é melhor que complexo', 'Diante da ambigüidade, recuse a tentação de adivinhar', 'Você sabe tudo isso?', 'Bonito é melhor que feio', 'Explícito é melhor que implícito', 'Simples é melhor que complexo', 'Complexo é melhor que complicado', 'Plano é melhor que aninhado', 'Dispersa é melhor que denso', 'Legibilidade conta', 'Casos especiais não são especiais o suficiente para quebrar as regras', 'Embora praticidade vença pureza', 'Erros nunca devem passar silenciosamente', 'A menos que explicitamente silenciados', 'Diante da ambigüidade, recuse a tentação de adivinhar', 'Não deve haver um', 'e de preferência apenas uma maneira', 'óbvia para fazê-la', 'Apesar de que maneira pode não ser óbvio à primeira vista, a menos que você seja holandês', 'Agora é melhor do que nunca', 'Embora nunca tenha sido muitas vezes é melhor do que agora', 'Se a implementação é difícil de explicar, é uma má idéia', 'Se a implementação é fácil de explicar, pode ser uma boa idéia', 'Os espaços de nomes são uma buzina de grandes ideias. Vamos fazer mais daqueles!', 'Eu concordo']        
		'''
		self.trainer.train(conversa)
		self.trainer.train(conversa2)
		self.trainer.train(conversa3)
		self.trainer.train(conversa4)
		self.trainer.train(conversa5)
		self.trainer.train(conversa6)
		self.trainer.train(conversa7)
		self.trainer.train(conversa8)
		for treino in os.listdir(nome_pasta):
			self.trainer.train(nome_pasta + treino)
		'''   