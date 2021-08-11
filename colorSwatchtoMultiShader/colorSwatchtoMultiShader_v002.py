import c4d
from c4d import gui
from c4d.modules import colorchooser
import maxon

# Welcome to the world of Python
# Main function
def main():
    swatchData = colorchooser.ColorSwatchData()
    if swatchData is None:
      return
  
    swatchData.Load(doc)
    
    if swatchData.GetGroupCount(c4d.SWATCH_CATEGORY_DOCUMENT) == 0:
        gui.MessageDialog("Please add a swatch group.")
        return
        
    swatchGroup = swatchData.GetGroupAtIndex(0,c4d.SWATCH_CATEGORY_DOCUMENT)
    swatchColorCount = swatchGroup.GetColorCount()

    mat = c4d.BaseMaterial(c4d.Mmaterial)
    mat.SetName("MultiShader")
    shader = c4d.BaseList2D(1019397)
    mat.InsertShader(shader)
    doc.InsertMaterial(mat)
    mat[c4d.MATERIAL_COLOR_SHADER] = shader
    
    for x in range(swatchColorCount):
 
        texSteps = 1050 + x
        if x > 1:
            c4d.CallButton(shader,c4d.MGMULTISHADER_ADD)
        colorShader = c4d.BaseList2D(5832)
        mat.InsertShader(colorShader)
        
        swatchColor = swatchGroup.GetColor(x)
        swatchRGB = c4d.Vector(swatchColor[0].r, swatchColor[0].g, swatchColor[0].b)
        
        mat[c4d.MATERIAL_COLOR_COLOR] = swatchRGB
        colorShader[c4d.COLORSHADER_COLOR] = swatchRGB
        shader[texSteps] = colorShader
        
    
    
    #gui.MessageDialog(swatchRGB)

# Execute main()
if __name__=='__main__':
    main()
