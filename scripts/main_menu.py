from bge import logic

scene = logic.getCurrentScene()
AVATARS = ['AvatarManiek' , 'AvatarJenifer']

avatarVisibleIndex = 0

def playActions():
    global avatarVisibleIndex
    scene = logic.getCurrentScene()

    avatars = [ x for x in scene.objects if 'Avatar' in str(x) ]

    for avatar in avatars:
        avatar.suspendDynamics()
        avatar.playAction( 'maniek_menu' , 0 ,507 , play_mode=1 )

    avatars[ avatarVisibleIndex ].setVisible(True, True)
    evee = scene.objects['evee_skeleton']
    evee.playAction( 'evee_menu' , 0 ,507 , play_mode=1 )

    # avatar_animation.setParent(avatar)

def change_avatar():
    global avatarVisibleIndex
    avatarVisibleIndex+=0.5

    if avatarVisibleIndex % 1 == 0:
        update_visible_avatar( )


def update_visible_avatar( ):
    global avatarVisibleIndex
    index = int(avatarVisibleIndex)
    scene = logic.getCurrentScene()
    avatars = [ x for x in scene.objects if 'Avatar' in str(x) ]
    for avatar in avatars:
        avatar.setVisible(False, True)

    try:    
        avatars[ index ].setVisible(True, True)
    except :
        avatarVisibleIndex = 0
        update_visible_avatar( )