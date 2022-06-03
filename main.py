from xml.dom.minidom import Element
import numpy as np

outputEle = Element('my-array').element

console.log(outputEle)


arr = np.ones(4)
outputEle.innerHTML = f"{arr}"
