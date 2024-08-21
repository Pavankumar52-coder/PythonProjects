import cloudinary
import cloudinary.uploader

cloudinary.config(
    cloud_name='dlykj6hym',
    api_key='537657574456794',
    api_secret='YED35_zTQryWoiOmT3_if1Xl98s'
)

try:
    response = cloudinary.uploader.upload('download.jpeg')
    print(response)
except Exception as e:
    print(f'Error: {str(e)}')