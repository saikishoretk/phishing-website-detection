import FeatureExtraction
import numpy as np
data = FeatureExtraction.getAttributess('http://asesoresvelfit.com/media/datacredito.co/')
print(data)
data.to_csv('file_name.csv', encoding='utf-8')
#np.savetxt('file.txt', data)
