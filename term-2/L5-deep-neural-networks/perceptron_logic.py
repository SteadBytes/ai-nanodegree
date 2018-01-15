import pandas as pd

# Demonstration of using Perceptrons as Logical Operators


class Perceptron:
    def __init__(self, weights, bias, out_func=lambda x: x >= 0):
        """
        Args:
            weights (list or tuple): input weight values w[0...n]
            bias (int or float): *b* value in Wx+b linear combination
            out_func (function): Function applied to the result of linear
                combination. Default= step function: lambda x: x >= 0
                Must return Bool. 
        """
        self.weights = weights
        self.bias = bias
        self.out_func = out_func

    def linear_combination(self, inputs):
        """ Calculate Wx+b
        Args:
            inputs (list or tuple): x values x[0...n]
        """
        linear_combination = self.bias
        for x, w in zip(inputs, self.weights):
            linear_combination += x * w
        return linear_combination

    def calc(self, inputs):
        return self.out_func(self.linear_combination(inputs))


def test_single_perceptron(perceptron, test_inputs, test_outputs):
    outputs = []
    columns = ['Input 1', '  Input 2', '  Linear Combination',
               '  Activation Output', '  Is Correct']
    for test_input, correct_output in zip(test_inputs, correct_outputs):
        linear_combination = perceptron.linear_combination(test_input)
        output = perceptron.calc(test_input)
        is_correct_string = 'Yes' if output == correct_output else 'No'
        outputs.append([test_input[0], test_input[1],
                        linear_combination, output, is_correct_string])
    display_results(outputs, columns)


def display_results(outputs, columns):
    output_frame = pd.DataFrame(outputs, columns=columns)
    print(output_frame.to_string(index=False))


test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]

and_perceptron = Perceptron((1, 1), -2)
correct_outputs = [False, False, False, True]
print('AND Perceptron:')
test_single_perceptron(and_perceptron, test_inputs, correct_outputs)

not_perceptron = Perceptron((0, -1), 0.5)
correct_outputs = [True, False, True, False]
print('NOT Perceptron:')
test_single_perceptron(not_perceptron, test_inputs, correct_outputs)

or_perceptron = Perceptron((2, 2), -2)
correct_outputs = [False, True, True, True]
print('OR Perceptron:')
test_single_perceptron(or_perceptron, test_inputs, correct_outputs)

print('NAND Multilayer Perceptron:')
correct_outputs = [True, True, True, False]
outputs = []
for test_input, correct_output in zip(test_inputs, correct_outputs):
    # NAND is an AND followed by NOT
    and_res = and_perceptron.calc(test_input)
    output = not_perceptron.calc((0, and_res))
    is_correct_string = 'Yes' if output == correct_output else 'No'
    outputs.append([test_input[0], test_input[1], output, is_correct_string])
display_results(outputs, ['Input 1', '  Input 2', '  Activation Output',
                          '  Is Correct'])
