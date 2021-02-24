from bge import logic


def playActions():

    scene = logic.getCurrentScene()

    avatar = [ x for x in scene.objects if 'Avatar' in str(x) ][0]
    evee = scene.objects['evee_skeleton']

    avatar.playAction( 'maniek_menu' , 0 ,507 , play_mode=1 )
    evee.playAction( 'evee_menu' , 0 ,507 , play_mode=1 )

    # avatar_animation.setParent(avatar)