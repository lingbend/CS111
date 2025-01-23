# CS111
BYU CS 111 class

## Homework 1: Admission Data Processing
Intakes student data from a csv file, parses it, and scores it according to various algorithms, outputting each result as a file.
check_row_types function provided in assignment.

This project demonstrates data parsing, complex algorithms, and file i/o.

## Homework 5: Mergesort
Implements mergesort from commandline inputs of the form mergesort.py input_file output_file_name.
Tests provided in assignment.

This project demonstrates mergesort and recursive programming.

## Project 1: Image transformations
Processes image via commandline. Modes:
-d image_file: display mode - shows the image
-k input_image output_file_name percent_dark_float(1-0): darken mode
-s input_image output_file_name: sepia mode
-g input_image output_file_name: grayscale mode
-b input_image output_file_name border_thickness(int) rgb_red_value rgb_green_value rgb_blue_value: border mode (makes borders of the specified rgb color and pixel thickness)
-f input_image output_file_name: flip mode (flips on the x-axis)
-m input_image output_file_name: mirror mode (mirrors across y-axis)
-c input_image_1 input_image_2 input_image_3 input_image_4 output_file_name border_thickness(int): collage mode (makes a collage of 4 images with black borders of the input thickness in pixels around each image)
-y foreground_image background_image output_file_name minimum_green_value(int 0-255) factor_above_saturation: green screen mode (replaces the green background with the background image, detecting the screenscreen using the threshold and minimum green values) 

This project demonstrates image manipulation, RGB, passing functions as arguments, file i/o, and looping.

## Project 2: Grid Class for Sand Simulator
I created the Grid class (Grid.py) for this sand simulation. The sand simulation (sand_oo.py) was created by Stanford for their CS106A and provided through BYU.

This project demonstrates OOP, integration with prewritten technology, exception handling, and usings arrays to create grid data structures.

## Project 3: Calculator and Input Parser
Calculator using Lisp-style Polish notation (ie. 9 + 10 * 9 would be written as (+ 9 (* 10 9))). Some of pair.py was prewritten by BYU including Nil. Most of calculator.py was programmed by me, although the algorythm was provided by BYU. 
To use run calculator.py and input expressions in the form explained before. Input "exit" to end. Supports the operations "*", "/", "+", and "-".

This project demonstrates parsing, exception handling, recursive functions, and OOP.

## Project 4: Webcrawler
This is a webcrawler with 3 modes:
webcrawler.py -c root_url output_png output_csv: Counts how many times each page is linked in root and on those linked pages recursively unless they have a different root, not counting the links on pages with a different root. Outputs the results as a png using pyplot and a csv file.
webcrawler.py -p url output_png output_csv: Searches for a table with id "CS111-Project4b", graphs the data in a png, and outputs the data as a csv.
webcrawler.py -i url output_file_prefix (-s/-g/-f/-m): This uses the image processing functions from project 1 to modify images extracted from the url. The new files are renamed using the prefix -s is sepia, -g is grayscale, -f is flip about x, and -m is flip about y.

The RequestGuard class prevents the crawler from visiting other domains.

This project demonstrates the use of regex, exception handling, pyplot, webcrawling, file i/o, and bs4.

Note: This project was designed and tested specifically for BYU's CS111 website.