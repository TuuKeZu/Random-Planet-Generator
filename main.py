from os import read
from PIL import Image, ImageFont, ImageDraw 
from planetNameRandomizer import generateRandomName
import random
from datetime import date
import timeit
import math

today = date.today()

img = Image.open('./input/3.png')
pixelmap = img.load()

print(img.size)

imgNew = Image.new( 'RGB', img.size )
pixelmapNew = imgNew.load()

font = ImageFont.truetype('fonts/font2.ttf', 80, encoding="unic");
generator = generateRandomName()

nameEntries = [];
setNames = ['Emelina', 'Ivo', 'Fachtna', 'Havel', 'Romualdo', 'Miguel', 'Pablo', 'Izydor', 'Amanda', 'Aguli'];


randomRange = [-170, 170]
dataRange = [0, 220]
blackFilter = 50
numberOfEntries = 10
path = "./images/"



# Shift the color of the picture with weighted random for each RGB values.
#E.g. [-255, -255, 255] would only return blue planets etc.
def colorShift(index, weightedRandom):

    # generate random color multiplier with weighted value.
    shiftRange = [random.randrange(randomRange[0], randomRange[1]) + weightedRandom[0],
    random.randrange(randomRange[0], randomRange[1]) + weightedRandom[1],
    random.randrange(randomRange[0], randomRange[1]) + weightedRandom[2]];

    # shift the color of each pixel
    for i in range(img.size[0]):
        for e in range(img.size[1]):
            pixel = pixelmap[i ,e]
            newColor = [0] * 3
            average = (pixel[0] + pixel[1] + pixel[2]) / 3

            if(average > blackFilter):

                for c in range(3):
                    color = pixel[c]
                    Ncolor = color + shiftRange[c]

                    if(color + Ncolor >= dataRange[0] and color + shiftRange[c] <= dataRange[1]):
                        newColor[c] = color + shiftRange[c]
                    else:
                        if(color + shiftRange[c] > dataRange[1]):
                            newColor[c] = dataRange[1]
                        elif(color + shiftRange[c] < dataRange[0]):
                            newColor[c] = dataRange[0]

                result = (newColor[0], newColor[1], newColor[2], 255)
                
            else:
                result = pixel
                    
            pixelmapNew[i, e] = result

    # save the image
    imgNew.save(f"{path}/img-{index}.png")

# Generate a rabndom name and render it on the image
def generateName(index):
    
    name = generator.generateName()

    while(name in nameEntries):
        print("Drean luck alert - Dublicate name detected!")
        name = generator.generateName();
    
    nameEntries.append(name);

    img = Image.open(f"{path}/img-{index}.png")
    draw = ImageDraw.Draw(img)

    w, h = draw.textsize(name, font)

    draw.text(((img.size[0] - w) / 2, ((img.size[1] - h) / 2) + 300), name, img.load()[452, 552], font=font)
    img.save(f"{path}/img-{index}.png");
    return True


# Force the name from setNames-list
def setName(index):
    name = setNames[index]
    nameEntries.append(name)

    img = Image.open(f"{path}/img-{index}.png")
    draw = ImageDraw.Draw(img)

    w, h = draw.textsize(name, font)


    draw.text(((img.size[0] - w) / 2, ((img.size[1] - h) / 2) + 300), name, img.load()[452, 552], font=font)
    img.save(f"{path}/img-{index}.png");
    return True

#log the output in the output.txt
def logOut():
    f = open("output.txt", "w")
    f.write(f"Generated on {today}\n")
    f.write("Tuukka Moilanen 2021 - all rights recerved.\n")
    f.write("-" * 30 + "\n")

    for i in range(numberOfEntries):
        f.write(nameEntries[i] + "\n")
    
    f.close()

# check for dublicates. Useful when dealing with 1000's of images and want to make sure there's no dublicates
def anydup(thelist):
  seen = set()
  for x in thelist:
    if x in seen:
        print(x)
    seen.add(x)
  return False

# validate all the images from current generation
def validate():
    print(f"Went through {len(nameEntries)} names!");
    print(anydup(nameEntries));


# main fuction responsible for actually managing generation
def generateImages():
    print("ColorShifter v1.0 - Initializing Setup...")
    print("-" * 30)
    print(f"Entries: {numberOfEntries}");
    print(f"Path: {path}")

    # generate the initial image and log the time used for one generation.
    e_start = timeit.default_timer()
    colorShift(0, [0, 0, 0])
    setName(0)
    e_stop = timeit.default_timer()

    estimate = numberOfEntries * (e_stop - e_start)
    estimateMins = estimate / 60

    if(math.floor(estimateMins) >= 1):
        estimateS = f"{estimateMins}min"
    else:
        estimateS = f"{estimate}s"
    
    print(f"Estimated time for the generation: {estimateS}")
    input("Press Enter to Start...")
    start = timeit.default_timer();

    chunk = numberOfEntries / 3;

    # Split the generationm into 3 phases; [blue, green, red]
    # Verify the dublicates between each generation.
    for i in range(numberOfEntries):
        if(i % math.floor(numberOfEntries / 3) == 0):
            validate()

        if(0 < i <= chunk * 1):
            colorShift(i, [-50, -50, 250])
        elif(chunk < i <= chunk * 2):
            colorShift(i, [-50, 250, -50])
        elif(chunk * 2 <= i < chunk * 3):
            colorShift(i, [250, -50, -50])

        generateName(i);
        print(f"Done - {i}/{numberOfEntries} - {nameEntries[i]}")


    img.close()
    imgNew.close()

    stop = timeit.default_timer();
    timed = stop - start
    print(f"Finished The Generation : {numberOfEntries} entries were generated in {timed}!")


generateImages()



        
