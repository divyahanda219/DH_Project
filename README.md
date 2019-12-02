### Project Rationale 

Animal behavior and health are closely related to each other. Monitoring animals can give an insight into animal health.Traditionally, the producers rely on humans to monitor their animals. This practice is time consuming and prone to human pereception errors. In a commercial farm the average attention received is around 3sec/animal. Some studies have made use of thermal cameras, kinetic sensors, drawing ink patterns etc to track animals. However, these methods are expensive and can not be replicated in commercial farm setup.

In this project, we use Machine learning algorithm Mask R-CNN to train our model to track pigs in a commercial farm set up. The only expense required is setting up of a camera (any) at the farm to collect data. The method suggested by us:
   * Is economical
   * Doesnot interefere with farm activities
   * Is independent of human biases and errors
   * Can act as decision making tool 

### After following this tutorial you will know how to:
  * Extract images from videos
  * Annotate your images
  * Train your model to detect the class specified by you
  * Evaluate the model you trained
  

### What is Machine Learning?

Machine Learning is a techonology that gives the computers the "ability to learn". Machine learning algorithms build a mathematical model based on sample data, known as "training data", in order to make predictions or decisions without being explicitly programmed to perform the task. To dive deeper into what is machine learning, you can refer to [this video](https://royalsociety.org/topics-policy/projects/machine-learning/videos-and-background-information/). 

In this module, we will train our computer to identify and track pigs. 

### What is Mask R-CNN?

Mask R-CNN is a machine learning algorithm that predicts the presence of an object in an image by generating bounding boxes and masks. There are two stages of Mask RCNN. First, it generates proposals about the regions where there might be an object based on the input image. Second, it predicts the class of the object, refines the bounding box and generates a mask in pixel level of the object based on the first stage proposal. Here is an example of what the image looks like after detection. 

![Check Readme if image doesn't open](https://raw.githubusercontent.com/divyahanda219/DH-Project-Website/master/MaskRCNN.png "Source: Mask RCNN paper")

### Data description

The data for this project consists of day and night videos of pigs from a commerical pig farm in Iowa. The videos were recorded using a simple camera.To get the data ready for Mask R-CNN algorithm, we will first extract images from the videos. You could also download images from google or any other source depending on the requirements of your project. Check out the code below for extracting images or you could download it from [here](https://github.com/divyahanda219/DH-Project-Website/blob/master/Extractimages.py).

Usually, a lot of images are required to train a model. But here, we are going to take advantage of transfer learning (expalined below). So, for this project we initially decided to use 70 images. But because this is computationally intensive, we reduced the number of images to 48. 40 for training and 8 for validation. Check out some of the images below that we used for this project.

Tip- After running the training we realized that it is better to reduce the dimensions of the images and then proceed any further. For this module however, image size was not reduced. 

### Transfer learning
Transfer learning simply means that we are not training the model from scratch. We rely on weights file that has already been trained to identify a variety of other classes. Here, we will use weights from COCO dataset. We have added the weights file in github repo. COCO dataset is a dataset that contains nearly 120k images, so the weights have learned to identify a lot of different objects. You can find the list of classes that COCO dataset is trained to identify [here](https://github.com/amikelive/coco-labels/blob/master/coco-labels-paper.txt). 

So now, we know that we don't need thousands of images (not always though) to train our model. Also, we know that COCO dataset doesnot contain a class for pig identification. Our next step is to get our images ready for processing.

Note - Before we move any further, we want to thank team Matterport for sharing the code for training own data using Mask R-CNN. We adapted and modified their code to suit our project. You can find the original code [here](https://github.com/matterport/Mask_RCNN).  
    
### Annotating the images

Mask R-CNN model requires that the images be annotated to specify the area of interest in image. We used VIA [VGG Image Annotator](http://www.robots.ox.ac.uk/~vgg/software/via/). This is a little time consuming part. Below is how our annotated file looked like:

![Check Readme if image doesn't open](https://raw.githubusercontent.com/divyahanda219/DH-Project-Website/master/annotated.png)


Once the annotation is done, download the json file. Split the annotated images into training and validation sets.  

### Training the Model

Our model is now ready to be trained. We used the [balloon.py](https://github.com/matterport/Mask_RCNN/blob/v2.1/samples/balloon/balloon.py) code by Matterport to train our model. You can find our complete code here. To train our model, we set 30 iterations of 100 epochs each. 

Use the following command to train the model. 

```
python Pig.py train --dataset=/path/to/dataset --weights=coco

## Incase, you wish to continue training from where you left off, use:

python Pig.py train --dataset=/path/to/dataset --weights=last
```

Training the model is computationally intensive. We suggest using gpu and not cpu for this purpose. It took us around 4 hours to train our model. The size of images also plays a role in time consumed. After the training is complete, you should get a trained weights file. When we finished training, a loss of 0.2082 (shown below) was reported. 

![Refer to Readme if image doesn't open](https://raw.githubusercontent.com/divyahanda219/DH-Project-Website/master/LossFunction.png)

### Evaluate the model

To evaluate the model, load the trained weights file and the model. Run the detection. We used [inspect model](https://github.com/matterport/Mask_RCNN/blob/v2.1/samples/balloon/inspect_balloon_model.ipynb. But since we were more interested to run the detection on videos we added a few extra steps [inspired by](https://www.dlology.com/blog/how-to-run-object-detection-and-segmentation-on-video-fast-for-free). You can find our complete code here. The processing of videos will be done on frame by frame basis, meaning that detection will be run for each frame of the video. Now, you could also change that and instead batch process every 3 frames or more (depending on your system). But because our images were too large and system not too fast, we stuck to processing one frame at a time. Below is an example of how the detection looked like in one of the frames: 

![Refer to Readme if image doesn't open](https://raw.githubusercontent.com/divyahanda219/DH-Project-Website/master/Detection.png)

Once the images are processed (ran detection), we process the images back to a video and an output video contatining detections is generated.     


### Class Exercise

In each project, I'd like to see a homework assignment that the class can do/evaluate to learn more about your data.  This should be a reproducible notebook that allows them to learn one or more aspects of your data workflow.  It is also an opportunity to share your research with your colleagues.

Here is an example of a fantastic project website:

https://stephenslab.github.io/ipynb-website/

## Advanced Features

### Stylesheet (Advanced)

If you'd like to add your own custom styles:

1. Create a file called `/assets/css/style.scss` in your site
2. Add the following content to the top of the file, exactly as shown:
    ```scss
    ---
    ---

    @import "{{ site.theme }}";
    ```
3. Add any custom CSS (or Sass, including imports) you'd like immediately after the `@import` line

*Note: If you'd like to change the theme's Sass variables, you must set new values before the `@import` line in your stylesheet.*

### Layouts (Advanced)

If you'd like to change the theme's HTML layout:

1. [Copy the original template](https://github.com/pages-themes/slate/blob/master/_layouts/default.html) from the theme's repository<br />(*Pro-tip: click "raw" to make copying easier*)
2. Create a file called `/_layouts/default.html` in your site
3. Paste the default layout content copied in the first step
4. Customize the layout as you'd like

### Overriding GitHub-generated URLs (Advanced)

Templates often rely on URLs supplied by GitHub such as links to your repository or links to download your project. If you'd like to override one or more default URLs:

1. Look at [the template source](https://github.com/pages-themes/slate/blob/master/_layouts/default.html) to determine the name of the variable. It will be in the form of `{{ site.github.zip_url }}`.
2. Specify the URL that you'd like the template to use in your site's `_config.yml`. For example, if the variable was `site.github.url`, you'd add the following:
    ```yml
    github:
      zip_url: http://example.com/download.zip
      another_url: another value
    ```
3. When your site is built, Jekyll will use the URL you specified, rather than the default one provided by GitHub.

*Note: You must remove the `site.` prefix, and each variable name (after the `github.`) should be indent with two space below `github:`.*

For more information, see [the Jekyll variables documentation](https://jekyllrb.com/docs/variables/).


### Contributing (Advanced)

Interested in contributing to Slate? We'd love your help. Slate is an open source project, built one contribution at a time by users like you. See [the CONTRIBUTING file](docs/CONTRIBUTING.md) for instructions on how to contribute.

### Previewing the theme locally

If you'd like to preview the theme locally (for example, in the process of proposing a change):

1. Clone down the theme's repository (`git clone https://github.com/pages-themes/slate`)
2. `cd` into the theme's directory
3. Run `script/bootstrap` to install the necessary dependencies
4. Run `bundle exec jekyll serve` to start the preview server
5. Visit [`localhost:4000`](http://localhost:4000) in your browser to preview the theme

### Running tests

The theme contains a minimal test suite, to ensure a site with the theme would build successfully. To run the tests, simply run `script/cibuild`. You'll need to run `script/bootstrap` one before the test script will work.
