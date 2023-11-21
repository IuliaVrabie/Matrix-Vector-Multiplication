# app.py
from flask import Flask, render_template, session, url_for, redirect
from flask_session import Session

app = Flask(__name__)

app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

input_index = 0
# matrix = [
#     [1, 2, 1, 3],
#     [1, -1, 2, -2],
#     [4, 3, 2, 1]
# ]
# vector = [1, 2, 3, 4]

matrix = [
    [3, 4, 5],
    [2, 5, 1],
    [2, 0, 9]
]
vector = [5, 9, 4]

cells = [{'c': 0, 'm_in': None, 'm_out': None, 'v_in': None, 'v_out': None} for _ in range(len(matrix))]
add_delay = False


def add_delays(a):
    for index, row in enumerate(a):
        # Prepend *'s as delays
        row[:0] = ['*'] * (len(a) - index - 1)

    return a

def add_zeros_to_matrix(matrix, vector):
    max_length = max(len(row) for row in matrix)

    for row in matrix:
        zeros = max_length - len(row)
        row.extend([0] * (max_length - len(row)))

    vector = vector + [0] * zeros
    return matrix, vector


@app.route('/')
def index():
    global matrix
    global add_delay, cells

    if add_delay is False:
        new_matrix = add_delays(matrix)
        session['new_matrix'] = new_matrix
        add_delay = True

    return render_template('index.html', cells=cells, matrix=session['new_matrix'], vector=vector)


@app.route('/next_step')
def next_step():
    global input_index, cells, vector
    matrix = session['new_matrix']
    matrix, vector = add_zeros_to_matrix(matrix, vector)

    # First propagate the input
    for i in range(len(cells)):
        if input_index < len(vector):
            cells[i]['m_in'] = matrix[i][input_index]
        else:
            cells[i]['m_in'] = 0

        if i < len(cells) - 1:
            cells[i]['v_in'] = cells[i + 1]['v_out']
        else:
            if input_index < len(vector):
                cells[i]['v_in'] = vector[input_index]
            else:
                cells[i]['v_in'] = 0

    for cell in cells:
        for key in cell:
            if cell[key] is None:
                cell[key] = 0

    for i in range(len(cells)):
        if cells[i]['m_in'] == '*':
            cells[i]['m_in'] = 0
        if cells[i]['m_out'] == '*':
            cells[i]['m_out'] = 0

    # Execute the algorithm and update the register and the out
    for i in range(len(cells)):
        cells[i]['c'] += cells[i]['m_in'] * cells[i]['v_in']
        cells[i]['m_out'] = cells[i]['m_in']
        cells[i]['v_out'] = cells[i]['v_in']

    input_index += 1

    return render_template('index.html', cells=cells, matrix=session['new_matrix'], vector=vector)


@app.route('/clear')
def clear():
    global add_delay
    print(add_delay)
    session.clear()

    add_delay = False
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
