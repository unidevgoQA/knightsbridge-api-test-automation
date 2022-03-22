from pathlib import Path

test_image = Path(__file__).parent / 'test.jpg'

file = {
    'media': (test_image, open(test_image, 'rb')),
    'bucketName': 'custom-coin',
    'type': 'image/jpeg'
}
