layer_name = ''

layer = QgsProject.instance().mapLayersByName(layer_name)[0]
layer.startEditing()

field_name = ''
field_index = layer.fields().indexFromName(field_name)
if field_index == -1:
    layer.addAttribute(QgsField(field_name, QVariant.String))

for feature in layer.getFeatures():
    sand = feature['Sand']
    clay = feature['Clay']
    silt = feature['Silt']

    if sand >= 0 and sand <= 45 and clay >= 40 and clay <= 100 and silt >= 0 and silt <= 40:
        feature[field_name] = 'Cl'
    elif sand <= 65 and sand >= 45 and clay >= 35 and clay <= 55 and silt >= 0 and silt <= 20:
        feature[field_name] = 'SaCl'
    elif sand >= 0 and sand <= 20 and clay >= 40 and clay <= 60 and silt >= 40 and silt <= 60:
        feature[field_name] = 'SiCl'
    elif sand >= 20 and sand <= 45 and clay >= 25 and clay <= 40 and silt >= 15 and silt <= 55:
        feature[field_name] = 'ClLo'
    elif sand >= 0 and sand <= 20 and clay >= 25 and clay <= 40 and silt >= 40 and silt <= 75:
        feature[field_name] = 'SiClLo'
    elif sand >= 45 and sand <= 80 and clay >= 20 and clay <= 35 and silt >= 0 and silt <= 25:
        feature[field_name] = 'SaClLo'
    elif sand >= 25 and sand <= 55 and clay >= 5 and clay <= 25 and silt >= 25 and silt <= 50:
        feature[field_name] = 'Lo'
    elif sand >= 85 and sand <= 100 and clay >= 0 and clay <= 10 and silt >= 0 and silt <= 15:
        feature[field_name] = 'Sa'
    elif sand >= 70 and sand <= 90 and clay >= 0 and clay <= 15 and silt >= 0 and silt <= 30:
        feature[field_name] = 'LoSa'
    elif sand >= 45 and sand <= 85 and clay >= 0 and clay <= 20 and silt >= 0 and silt <= 50:
        feature[field_name] = 'SaLo'
    elif sand >= 0 and sand <= 50 and clay >= 0 and clay <= 25 and silt >= 50 and silt <= 85:
        feature[field_name] = 'SiLo'
    elif sand >= 0 and sand <= 20 and clay >= 0 and clay <= 15 and silt >= 80 and silt <= 100:
        feature[field_name] = 'y'
    else:
        feature[field_name] = 'n'

    layer.updateFeature(feature)

layer.commitChanges()
