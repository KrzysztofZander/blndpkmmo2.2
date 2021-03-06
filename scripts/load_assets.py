from bge import logic


def load(file):

    # Load blend file |  async == True crash application
    path = logic.expandPath('//assets/' + file + '.blend' )
    logic.LibLoad(path, 'Scene' , load_actions=True, load_scripts=True  )

def update_progres( fileNumber , numberOfFiles ):
    pass

def main():

    scene = logic.getCurrentScene()
    filesNeedToScene = {
        "mainMenu":[    'nature' , 
                        'avatars_maniek' , 
                        'avatars_jenifer',
                        'avatars_erika',
                        'avatars_chuck',  
                        'avatars_jimbo',
                        'avatars_mia',
                        'avatars_frankie',
                        'avatars_jasmina',
                        'avatars_mubutu',
                        'industrial', 
                        'evee'
                    ]
    }

    for files in filesNeedToScene[ scene.name ]:
        load( files )
    
    message = scene.name+'_loaded_assets'
    logic.sendMessage( message )

    

