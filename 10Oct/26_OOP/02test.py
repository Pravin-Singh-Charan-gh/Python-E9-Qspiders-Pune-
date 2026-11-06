def Vehicle(name,model,speed):
    name_ = name
    model_ = model
    speed_ = speed
    return {
        'setName': def setName(name):
            name_ = name
        ,
        def getName():
            return name_
        ,
        def setModel(model):
            model_ = model
        ,
        def getModel():
            return model_
        ,
        def setSpeed(speed):
            speed_ = speed
        ,
        def getSpeed():
            return speed_

    }
v1 = Vehicle('Scorpio','N',120)
