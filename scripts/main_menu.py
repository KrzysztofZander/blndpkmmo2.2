from bge import logic

scene = logic.getCurrentScene()
AVATARS = ['AvatarManiek' , 'AvatarJenifer' , 'AvatarJimbo' , 'AvatarErika' , 'AvatarChuck' , 'AvatarMia', 'AvatarFrankie', 'AvatarJasmina' , 'AvatarMubutu' ]

avatarVisibleIndex = 0

def playActions():
    global avatarVisibleIndex
    scene = logic.getCurrentScene()

    avatars = [ x for x in scene.objects if 'Avatar' in str(x) ]

    for avatar in avatars[:-1]:
        avatar.endObject()
    
    avatar = avatars[ 0 ]
    avatar.playAction( 'maniek_menu' , 0 ,507 , play_mode=1 )
    evee = scene.objects['evee_skeleton']
    evee.playAction( 'evee_menu' , 0 ,507 , play_mode=1 )

    # avatar_animation.setParent(avatar)

def next_avatar():
    global avatarVisibleIndex
    # Bge calls bnt twice , this is walkaround
    # each call has 0.5 value , so double click == 1
    
    avatarVisibleIndex+=0.5

    if avatarVisibleIndex % 1 == 0:
        update_visible_avatar( )

def prev_avatar():
    global avatarVisibleIndex

    # Bge calls bnt twice , this is walkaround
    # each call has 0.5 value , so double click == 1
    avatarVisibleIndex-=0.5

    print( avatarVisibleIndex )

    if avatarVisibleIndex % 1 == 0:
        update_visible_avatar( )


def update_visible_avatar( ):
    global avatarVisibleIndex
    index = int(avatarVisibleIndex)
    scene = logic.getCurrentScene()
    
    try:
        newAvatarName = AVATARS[index]
        print( newAvatarName )
        currentAvatar = [ x for x in scene.objects if 'Avatar' in str(x) ][0]

        position = currentAvatar.localPosition
        orientation = currentAvatar.localOrientation
        frame = currentAvatar.getActionFrame()
        
        currentAvatar.endObject()
        
        newAvatar = scene.addObject( newAvatarName )
        newAvatar.worldPosition[2] = 4
        newAvatar.localOrientation = orientation
        newAvatar.playAction( 'maniek_menu' , 0 ,507 , play_mode=1 )
        newAvatar.setActionFrame(frame)
    except Exception as e:
        print(e)
        avatarVisibleIndex = 0
        update_visible_avatar()