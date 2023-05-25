import pygame
import pygame.freetype
import sys

FPS=60
WINDOW_SIZE_X=800
WINDOW_SIZE_Y=600
TOTAL_TIME=100

# game states
GAME_STATE_MENU=1
GAME_STATE_PLAYING=2
GAME_STATE_EXIT=3
GAME_STATE_WIN=4
GAME_STATE_LOSS=5

def game_menu(resources):
    start_btn=resources['start_btn']
    exit_btn=resources['exit_btn']
    background=resources['background']
    screen=resources['screen']
    title=resources['title']

    start_btn=start_btn
    exit_btn=exit_btn

    going=True
    while going:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                going=False
                result=GAME_STATE_EXIT
            if event.type == pygame.MOUSEBUTTONDOWN:
                square=start_btn.get_rect().move(50, 300)
                if square.collidepoint(pygame.mouse.get_pos()):
                    going=False
                    result=GAME_STATE_PLAYING
                square=exit_btn.get_rect().move(75, 400)
                if square.collidepoint(pygame.mouse.get_pos()):
                    going=False
                    result=GAME_STATE_EXIT
        square=start_btn.get_rect().move(350, 300)
        if square.collidepoint(pygame.mouse.get_pos()):
            start_btn=start_btn
        else:
            start_btn=start_btn
        square=exit_btn.get_rect().move(400, 400)
        if square.collidepoint(pygame.mouse.get_pos()):
            exit_btn=exit_btn
        else:
            exit_btn=exit_btn
        screen.blit(background, background.get_rect())
        screen.blit(title, title.get_rect().move(400-250, 50))
        screen.blit(start_btn, start_btn.get_rect().move(50,300))
        screen.blit(exit_btn, exit_btn.get_rect().move(75,400))
        pygame.display.flip()
    return result

def game_playing(resources):
    overlay_font = resources['overlay_font']
    screen = resources['screen']
    player = resources['player']
    fontclic = resources['fontclic']
    poke = resources['poke']

    #rondes 
    primera = resources['primera']
    segunda = resources['segunda']
    boss = resources['boss']
    
    # atacar 
    atk_btn = resources['atacar']
    atk_esp = resources['especial']

    # victories 
    onewin = resources['onewin']
    twowin = resources['twowin']
    
    ## controlador de volum
    mute = resources['mute']
    unmute = resources['unmute']
    
    ## musica combat
    pygame.mixer.music.load("sounds/battlesound.wav")
    pygame.mixer_music.play()

    ###sons a un moment determinat
    raig=pygame.mixer.Sound("sounds/ray.wav")
    heal=pygame.mixer.Sound("sounds/heal.wav")

    ## tenda
    ## coins icon
    coins_icon = resources['coins_icon']
    #augmentar vida/temps
    pot = resources['pot']
    defensa = resources['defensa']

    clock = pygame.time.Clock()
    battle_time=0
    total_time=TOTAL_TIME
    clock_event = pygame.USEREVENT+1
    pygame.time.set_timer(clock_event, 120)
    ###fi rellotge
    result=GAME_STATE_PLAYING
    click=0
    ## iniciem coins compres tenda recursos   
    coins=0

    going=True
    while going:
        screen.fill((128,128,128))
        draw_shop(resources)
        delta=clock.tick(FPS)
        battle_time+=delta
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                going=False
                result=GAME_STATE_EXIT
                sys.exit()
            if event.type == clock_event:
                total_time-=1
                if total_time<=0:
                    result=GAME_STATE_LOSS
                    pygame.time.set_timer(clock_event, 0)
                    ########AGAFA BOTÓ CLIC##########
            if event.type == pygame.MOUSEBUTTONDOWN:
                ###captura nomes el boto esquerre del ratoli
                mouse_presses=pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    atacar=atk_btn.get_rect().move(320,300)
                    if atacar.collidepoint(pygame.mouse.get_pos()):
                        click += 1
                        ##cada placaje dona 3 coins per comprar a la tenda
                        coins += 2
                    #### atac especial que fa doble clic
                    especial=atk_esp.get_rect().move(320,360)
                    if especial.collidepoint(pygame.mouse.get_pos()):
                        click += 2
                        # musica de raig
                        pygame.mixer.Sound.play(raig)   
                    ##boto health +10 segons
                    aughealth=pot.get_rect().move(610,210)
                    if coins>=20:
                        if aughealth.collidepoint(pygame.mouse.get_pos()):
                            total_time = total_time + 10
                            coins = coins - 20
                            pygame.mixer.Sound.play(heal)
                    #boto defensa, augmenta el delay del temporitzador
                    ralent=defensa.get_rect().move(670,210)
                    if coins>=25:
                        if ralent.collidepoint(pygame.mouse.get_pos()):
                            coins = coins - 25
                            pygame.time.set_timer(clock_event, 140)
                    ####controlador de volum
                    # mutejar volum
                    desactivavol=unmute.get_rect().move(50,500)
                    if desactivavol.collidepoint(pygame.mouse.get_pos()):
                        pygame.mixer.music.set_volume(0.0)
                    activavol=unmute.get_rect().move(120,500)
                    if activavol.collidepoint(pygame.mouse.get_pos()):
                        pygame.mixer_music.set_volume(1.0)
        if coins<0:
            coins=0
        ##################RONDES#############
        #ronda 1 caterpie
        draw_overlay(screen, overlay_font, total_time, fontclic, click, mute, unmute, poke, atk_btn, coins, coins_icon)
        draw_player(screen, player)
        draw_shop(resources)
        primer_combat(screen, primera)
        ########## si fem 15 clics, pasem a la ronda 2 
        if click>14:
            screen.fill((128,128,128))
            draw_player(screen, player)
            draw_overlay(screen, overlay_font, total_time, fontclic, click, mute, unmute, poke, atk_btn, coins, coins_icon)
            draw_shop(resources)
            segon_combat(screen, segunda, onewin)
        #ronda 2 poliwhirl
        if click>30:
            screen.fill((229,172,71))
            draw_player(screen, player)
            draw_overlay(screen, overlay_font, total_time, fontclic, click, mute, unmute, poke, atk_btn, coins, coins_icon)
            draw_shop(resources)
            ultim_combat(screen, twowin, boss)
        ##pantalla final de guanyem
        if click>=60:
            pygame.mixer_music.stop()
            screen.fill((128,128,128))
            result=GAME_STATE_WIN
            going=False
        recursos_shop(screen, click, atk_esp, pot, defensa)

        if result==GAME_STATE_WIN:
            game_win(resources)
        if result==GAME_STATE_LOSS:
            game_loss(resources)
        if result==GAME_STATE_EXIT:
            game_exit(resources)
        pygame.display.flip()
    return result
def primer_combat(screen, primera):
    screen.blit(primera, primera.get_rect().move(300, 120))
def segon_combat(screen, segunda, onewin): 
    screen.blit(segunda, segunda.get_rect().move(300, 120))
    ###quadre rondes ganades
    screen.blit(onewin, onewin.get_rect().move(600, 400))
def ultim_combat(screen, twowin, boss):
    screen.blit(twowin, twowin.get_rect().move(600, 400))
    screen.blit(boss, boss.get_rect().move(300, 100))
def recursos_shop(screen, click, atk_esp, pot, defensa):
    ###compres
    ### apareix el segon atac especial
    if click>20:    
        screen.blit(atk_esp, atk_esp.get_rect().move(320, 360))
    screen.blit(pot, pot.get_rect().move(610,210))
    screen.blit(defensa, defensa.get_rect().move(670, 210))

def load_resources():
    resources = {}
    resources['game_icon']=pygame.image.load('images/favicon.png')
    resources['screen'] = pygame.display.set_mode([WINDOW_SIZE_X, WINDOW_SIZE_Y])
    resources['title']=pygame.image.load('images/menu/title.png')
    resources['start_btn']=pygame.image.load('images/menu/start_button.png')
    resources['exit_btn']=pygame.image.load('images/menu/exit_button.png')
    resources['background']=pygame.image.load('images/menu/background.jpg')
    resources['overlay_font']=pygame.freetype.Font("fonts/tlight.ttf", 46)
    resources['fontclic']=pygame.freetype.Font("fonts/tlight.ttf", 30)
    resources['player']=create_players()

    # combats rivals
    resources['primera']=pygame.image.load('images/rivals/round1.png')
    resources['segunda']=pygame.image.load('images/rivals/round2.png')
    resources['boss']=pygame.image.load('images/rivals/boss.png')
    
    #atacs 
    resources['atacar']=pygame.image.load('images/battle/atkbutton.png')
    resources['especial']=pygame.image.load('images/battle/atkesp.png')
    
    #comptador victories
    resources['onewin']=pygame.image.load('images/battle/onewin.png')
    resources['twowin']=pygame.image.load('images/battle/twowin.png')
    resources['wingame']=pygame.image.load('images/battle/wingame.png')
    resources['poke']=pygame.image.load('images/battle/poke.png')

    # mute o unmute volume 
    resources['mute']=pygame.image.load('sounds/mute.png')
    resources['unmute']=pygame.image.load('sounds/unmute.png')
 
    #shop 
    resources['shop']=pygame.image.load('images/shop/shop.png')
    resources['pot']=pygame.image.load('images/shop/pot.png')
    resources['defensa']=pygame.image.load('images/shop/def.png') 
    # coins
    resources['coins_icon']=pygame.image.load('images/shop/coins.png')   
    return resources
def draw_overlay(screen, font, total_time, fontclic, clicks, mute, unmute, poke, atk_btn, coins, coins_icon):
    # titol
    font.render_to(screen, (275, 25), 'Combat')
    # caixa placaje
    screen.blit(atk_btn, atk_btn.get_rect().move(320, 300))
    # rellotge
    font.render_to(screen, (380, 550), str(total_time))
    # guanyats separador 
    screen.blit(poke, (645,350))
    #comptador de clicks totals
    fontclic.render_to(screen, (50, 150), 'Atacs: ')
    fontclic.render_to(screen, (150, 150), str(clicks))
    # coins shop per recursos 
    fontclic.render_to(screen, (650, 300), str(coins))
    screen.blit(coins_icon, (600, 275))
    ## botons mute o unmute
    screen.blit(mute, (50,500))
    screen.blit(unmute, (120,500))
def create_players():
    player={
        'front': [
        pygame.image.load('images/player/pikachu.png')
        ],
        'sprite_index': 0,
        'x': 80,
        'y': 250
    }
    player['sprites']=player['front']
    return player
def draw_player(screen, player):
    sprite=player['sprites'][player['sprite_index']]
    square=sprite.get_rect().move(player['x'], player['y'])
    screen.blit(sprite, square)

def draw_shop(resources):
    # tenda
    screen = resources['screen']
    shop = resources['shop']
    screen.blit(shop, shop.get_rect().move(600,50))
def game_loss(resources):
    pygame.mixer_music.stop()
    overlay_font = resources['overlay_font']
    screen = resources['screen']
    going=True

    while going:
        screen.fill((128,128,128))
        overlay_font.render_to(screen, (300, 200), 'Has perdut!')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
def game_win(resources):
    # musica guanyem
    pygame.mixer.music.load("sounds/battlewin.wav")
    ##iniciem musica
    pygame.mixer_music.play()

    overlay_font = resources['overlay_font']
    screen = resources['screen']
    ## quadre guanyat
    wingame = resources['wingame']

    going=True
    
    while going:
        screen.fill((128,128,128))
        overlay_font.render_to(screen, (200, 100), 'Has guanyat!')
        screen.blit(wingame, wingame.get_rect().move(275, 250))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
def game_exit(resources):

    screen = resources['screen']
    going=True
    
    while going:
        screen.fill((128,128,128))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
def main():
    pygame.init()
    pygame.mixer.init()
    resources = load_resources()

    pygame.display.set_caption('iPokemon')
    pygame.display.set_icon(resources['game_icon'])

    game_state=GAME_STATE_MENU
    while game_state!=GAME_STATE_EXIT:
        if game_state==GAME_STATE_MENU:
            game_state=game_menu(resources)
            # juguem
        elif game_state==GAME_STATE_PLAYING:
            game_state=game_playing(resources)
            ## guanya
        elif game_state==GAME_STATE_WIN:
            game_state==game_win(resources)
            # perd
        elif game_state==GAME_STATE_LOSS:
            game_state==game_loss(resources)
    pygame.quit()
    sys.exit()
main()