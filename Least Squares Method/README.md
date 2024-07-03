# Least-squares-method
The method of least squares is a standard approach in regression analysis to approximate the solution of overdetermined systems (sets of equations in which there are more equations than unknowns) by minimizing the sum of the squares of the residuals (a residual being the difference between an observed value and the fitted value provided by a model) made in the results of each individual equation. The predictions could be obtained as follows:

$$\hat{y} = X \beta $$

Where $X$ is the **design matrix**, $\beta$ is the **parameter vector**, and $\hat{y}$ is the **prediction vector**. By introducing a **residual vector** like $\epsilon$ we can rewrite this equation based on the **observation vector** $y$:

$$y = X \beta + \epsilon$$

## Code 
This python script takes a set of inputs and their corresponding outputs, which we'll refer to as the x vector and y vector respectively, then it will draw the garph of all different polynomial approximations with different degrees.


An example of four points with coordinates (-1, 2), (0, -1), (1, 1), and (2, 0) are shown below:

| 0th Order Polynomial | 1st Order Polynomial |
| :------------------: | :------------------: |
|![Figure_0](https://github.com/RamtinMoslemi/Least-squares-method/assets/76493699/f29bed05-5ef6-440c-8ce5-bf7b2f5ba2a2) | ![Figure_1](https://github.com/RamtinMoslemi/Least-squares-method/assets/76493699/09be94e1-f196-4d95-9490-1fc2b5913ed6) | 
| **2nd Order Polynomial** | **3rd Order Polynomial** |
| ![Figure_2](https://github.com/RamtinMoslemi/Least-squares-method/assets/76493699/382ffb5a-54f1-44d5-a606-4d563303f20c) | ![Figure_3](https://github.com/RamtinMoslemi/Least-squares-method/assets/76493699/5f4e8685-8bfa-4d95-9e21-0016e9acf889) |
