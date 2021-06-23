import pygame
import random
import time

nomeJogador = input("Por favor, digite seu nome! \n")
emailJogador = input("Por favor, digite seu e-mail! \n")
with open('Nome_Email.txt','w') as arquivo:
    arquivo.write(nomeJogador+"\n")
    arquivo.write(emailJogador+"\n")

pygame.init()

icone = pygame.image.load("assets/corona.png")
pygame.display.set_caption("A Saga da Vacina")
pygame.display.set_icon(icone)
largura = 800
altura = 600
display = pygame.display.set_mode( (largura,altura) ) 
fps = pygame.time.Clock()
vacina = pygame.image.load("assets/vacina.png")
fundo = pygame.image.load("assets/fundo.jpg")
pessoa = pygame.image.load("assets/pessoa2.png")
corona = pygame.image.load("assets/corona.png")
corona2 = pygame.image.load("assets/corona.png")

#[INICIO] Cores
preto = (0,0,0)
branco = (255,255,255)
#[FIM] Cores

def placarVacina(totalVacina):
    font = pygame.font.SysFont(None,25)
    texto = font.render("Doses recebidas:"+str(totalVacina),True,branco)
    display.blit(texto,(0,15))

def placarDesvios(desvios):
    font = pygame.font.SysFont(None,25)
    texto = font.render("Desvios:"+str(desvios),True,branco)
    display.blit(texto,(0,0))

def text_objects(texto, fonte):
    textSurface = fonte.render(texto, True, preto)
    return textSurface, textSurface.get_rect()

def message_display(text):
    fonte = pygame.font.Font("freesansbold.ttf",50)
    TextSurf, TextRect = text_objects(text, fonte)
    TextRect.center = ((largura/2), (altura/2))
    display.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
    jogar()
    
def victory():
    pygame.mixer.music.stop()
    message_display("Você foi Imunizado, parabéns!")

def dead():
    pygame.mixer.music.stop()
    message_display("Você foi Infectado")


def jogar():
    contadorVacina = 0
    habilitaVacina = False

    desviosAux1 = 0
    desviosAux2 = 0

    pygame.mixer.music.load("assets/level1-step1.mp3")
    pygame.mixer.music.load("assets/level1-step1-evil.mp3")
    pygame.mixer.music.play(-1)
    
    pessoaPosicaoX = largura * 0.45
    pessoaPosicaoY = altura * 0.8
    pessoaLargura = 89
    movimentoX = 0

    vacinaPosicaoX = largura * 0.45
    vacinaPosicaoY = -102
    vacinaAltura = 102
    vacinaLargura = 102
    vacinaVelocidade = 4

    coronaPosicaoX = largura * 0.45
    coronaPosicaoY = -67
    coronaLargura = 62
    coronaAltura = 67
    coronaVelocidade = 4

    corona2PosicaoX = largura * 0.45
    corona2PosicaoY = -67
    corona2Largura = 62
    corona2Altura = 67
    corona2Velocidade = 4


    while True:
        pygame.display.update()
        #[INICIO] bloco de comando para verificar interação do usuário
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    movimentoX = -8
                elif evento.key == pygame.K_RIGHT:
                    movimentoX = 8 
            if evento.type == pygame.KEYUP:
                movimentoX = 0        


        #[FIM] bloco de comando para verificar interação do usuário
        display.fill(branco)
        display.blit(fundo, (0,0)) #inserir imagem na tela

        #[INICIO] Posição do jogador e do Corona
        pessoaPosicaoX = pessoaPosicaoX + movimentoX
        if pessoaPosicaoX < 0:
            pessoaPosicaoX = 0
        elif pessoaPosicaoX + 100 > 800:
            pessoaPosicaoX = 800 - 100


        display.blit(pessoa, (pessoaPosicaoX,pessoaPosicaoY))


        if vacinaPosicaoY > altura:
            vacinaPosicaoY= -102
            vacinaVelocidade += 0.25
            habilitaVacina = False
            vacinaPosicaoX = random.randrange(0,largura-102)

        if coronaPosicaoY > altura:
            coronaPosicaoY = -67
            coronaVelocidade += 0.25
            coronaPosicaoX = random.randrange(0,largura-62)
            desviosAux1 = desviosAux1 + 1

        if corona2PosicaoY > altura:
            corona2PosicaoY = -67
            corona2Velocidade += 0.25
            corona2PosicaoX = random.randrange(0,largura-62)
            desviosAux2 = desviosAux2 + 1

        desvios = desviosAux1 + desviosAux2    

        
        sorteia = random.randrange(0,100)
        if sorteia == 90 and habilitaVacina == False:
            habilitaVacina = True
        if habilitaVacina == True:
            display.blit(vacina, (vacinaPosicaoX,vacinaPosicaoY))
            vacinaPosicaoY = vacinaPosicaoY + vacinaVelocidade
            
        display.blit(corona, (coronaPosicaoX,coronaPosicaoY))
        coronaPosicaoY = coronaPosicaoY + coronaVelocidade

        display.blit(corona2, (corona2PosicaoX,corona2PosicaoY))
        corona2PosicaoY = corona2PosicaoY + corona2Velocidade
        #[FIM] Posição do jogador e do Corona

        #[INICIO] Análise de colisão
        if pessoaPosicaoY < coronaPosicaoY + coronaAltura:
            if pessoaPosicaoX < coronaPosicaoX and pessoaPosicaoX+pessoaLargura > coronaPosicaoX or coronaPosicaoX+coronaLargura > pessoaPosicaoX and coronaPosicaoX+coronaLargura < pessoaPosicaoX+pessoaLargura:
                dead()
        if pessoaPosicaoY < corona2PosicaoY + corona2Altura:
            if pessoaPosicaoX < corona2PosicaoX and pessoaPosicaoX+pessoaLargura > corona2PosicaoX or corona2PosicaoX+corona2Largura > pessoaPosicaoX and corona2PosicaoX+corona2Largura < pessoaPosicaoX+pessoaLargura:
                dead()        

        if pessoaPosicaoY < vacinaPosicaoY + vacinaAltura and habilitaVacina == True:
            if pessoaPosicaoX < vacinaPosicaoX and pessoaPosicaoX+pessoaLargura > vacinaPosicaoX or vacinaPosicaoX+vacinaLargura > pessoaPosicaoX and vacinaPosicaoX+vacinaLargura < pessoaPosicaoX+pessoaLargura:
                contadorVacina = contadorVacina + 1
                habilitaVacina = False  
                vacinaPosicaoY= -102    
                if contadorVacina == 2:
                    victory()

        #[FIM] Análise de colisão

        placarVacina(contadorVacina)
        placarDesvios(desvios)
        pygame.display.update()
        fps.tick(60)

jogar()