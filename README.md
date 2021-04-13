# Implementation

Adopted from ml-morph.

Use this tool to detect corners of the veg quadrats, rotate the image based on those detections to straighten the image, and crop to the inside of the quadrat. Heavy WIP currently. Model trains, but detection accuracy needs to improve. Current status is annotating additional images.

## Process
copy images to img_small

`python3 src/image-resize.py -i img_small -n 5`

`python3 src/preprocessing.py -i img_small`

`imglab -c train.xml train`

`imglab -c test.xml test`

`imglab --parts 'tl tr br bl' train.xml` <br>
 * draw bounding box
 * select bounding box
 * right click within bounding box and choose appropriate landmark

`imglab --parts 'tl tr br bl' test.xml`

`python3 src/detector_trainer.py -d train.xml -t test.xml -n 7 -w 79000 -e 0.001 -c 15`

`python3 src/shape_trainer.py`

predict on images outside of training set

`python3 src/prediction.py -i test -d detector.svm -p predictor.dat `

view results
`imglab output.xml`

