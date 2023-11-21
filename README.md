## Matrix-Vector Multiplication 

The matrix-vector multiplication logic in this application is implemented using a linear array approach. The linear array represents a sequence of cells, each responsible for a specific computation step. The algorithm follows these key steps:

### Prerequisites

Before running the program, ensure that you have Python and Flask installed. You can install Flask using the following command:

```bash
pip install Flask
```

### How to run

1. Run the Flask application by executing the `app.py` file.
    ```bash
    python app.py
    ```
2. Open a web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).


### Functionality

1. **Initialization:**
   - The input matrix, vector, and a linear array of cells are initialized.
   - Delays (represented by '*' symbols) can be added to the input matrix for visualization purposes.

2. **Propagation of Input:**
   - The algorithm starts by propagating the input values through the linear array.
   - Each cell in the linear array receives input from the corresponding element in the matrix and the neighboring cells.
   - The input values are updated in the cells for visualization.

3. **Calculation:**
   - The algorithm iterates through the linear array to perform calculations.
   - Each cell computes the product of its input matrix value and the corresponding vector value.
   - The intermediate result is accumulated in the cell.

4. **Updating Output:**
   - The algorithm updates the output values of the cells, representing the result of the multiplication process.
   - The output values are then displayed on the web page.

5. **Iteration:**
   - The user can step through the algorithm by clicking the "Next step" button.
   - The iteration continues until the entire matrix-vector multiplication is completed.

6. **Restart:**
   - Users can restart the process by clicking the "Restart" button, clearing the session and allowing for a fresh start.

### Cell Structure

Each cell in the linear array contains the following attributes:

- `m_in`: Input value from the matrix.
- `m_out`: Output value to be passed to the next cell.
- `v_in`: Input value from the vector or the previous cell's output.
- `v_out`: Output value to be passed to the next cell.
- `c`: Accumulated result of the multiplication process.

### Visualization

The web interface displays the matrix, vector, and the linear array of cells. The HTML template (`index.html`) uses Jinja templating to dynamically render the values and intermediate calculations. The user can observe how the algorithm processes the input and produces the final result.

### Interaction

- Clicking the "Next step" button iterates through the algorithm, providing a step-by-step visualization.
- The "Restart" button allows users to clear the session and start the matrix-vector multiplication process again.

### Customization

Users can experiment with different input matrices and vectors by modifying the `matrix` and `vector` variables in the `app.py` file. Additionally, the code can be extended to handle larger matrices or different multiplication strategies.

![First page](https://github.com/IuliaVrabie/Matrix-Vector-Multiplication/blob/2787871f4cf65de727565644fb6f20dce9583d7e/mvm.png)
