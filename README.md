features
========

This is a collection of feature extraction/selection algorithms. 

As an example, the following code generate two sets of examples sampled from the uniform distribution and then performs Kernel Canonical Correlation Analysis (KCCA) in the linear kernel space. The resulting dual directions for X and Y and given by alpha and beta respectively. See John Shawe-Taylor and Nello Cristianini, Kernel methods for pattern analysis, Cambridge University Press, 2004 for details.


:: 

    import numpy
    from features import KernelCCA
    from kernel import LinearKernel

    numExamples = 5
    numXFeatures = 10
    numYFeatures = 15
    X = numpy.random.rand(numExamples, numXFeatures)
    Y = numpy.random.rand(numExamples, numYFeatures)

    tau = 0.0
    kernel = LinearKernel()
    cca = KernelCCA(kernel, kernel, tau)
    alpha, beta, lmbdas = cca.learnModel(X, Y)


