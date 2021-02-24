from bge import logic

def replace():
    scene = logic.getCurrentScene()

    objects = [x for x in scene.objects if 'empty' in str(x)]

    for item in objects:

        try:
            replacedObject = item.name.split('empty_')[-1]

            scene.addObject( replacedObject , item )

            item.endObject()
        except:
            print('object ' , item , ' wont replaced')
    

    message = scene.name+'_replaced_assets'
    logic.sendMessage( message )

