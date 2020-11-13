def convolve2D(image, 
               kernel, 
               padding=0,
               strides=1):
    
    # Cross Correlation
    kernel = np.flipud(np.fliplr(kernel))

    # Gather Shapes of Kernel + Image + Padding
    x_ker, y_ker = kernel.shape
    x_size, y_size = image.shape[0:2]

    im_padded = np.pad(image, padding,  
                       mode='constant', 
                       constant_values=(0))
    
    # Initialize Output Convolution
    x_out = int(((x_size - x_ker + 2 * padding) / strides) + 1)
    y_out = int(((y_size - y_ker + 2 * padding) / strides) + 1)
    output = np.zeros((x_out, y_out))

    # Iterate through image
    for y in range(0, y_size - y_ker, strides):
        for x in range(0, x_size - x_ker, strides):
            # do the dot product
            output[x, y] = (kernel * im_padded[x: x + x_ker, y: y + y_ker]).sum()

    return output