# x = [12,1,34]
y_train = [20,40,60]
x_train = [1,2,3]
w = 10
b = 5

def model(x: list[int], w, b) -> list:
    preds = []
    for i in x:    
        y = w * i + b 
        preds.append(y)
    return preds

predictions = model(x_train,w,b)
# print('predictions', predictions)


def mse(actual: list[int], pred: list[int]) -> tuple:
    losses = []
    for i,j in zip(actual,pred):
        errors = (i - j) ** 2
        losses.append(errors)
    se = sum(losses) / len(actual)
            
    return losses, se

# print('losses and MSE:', mse(actual,predictions))


def gradient_w(w: int, b: int, x: list[int], actual_y: list[int]) -> tuple:
    derivatives = []
    for x_i, y_i in zip(x, actual_y):
        der = -2*x_i*(y_i - w * x_i - b)
        derivatives.append(der)
    gradient = sum(derivatives) / len(x)
    return derivatives,gradient

def gradient_b(pred_y: list[int], actual_y: list[int]):
    derivatives = []
    for y_i, j_y in zip(pred_y, actual_y):
        der = (j_y - y_i) * -2 
        derivatives.append(der)
    gradient_sum = sum(derivatives)
    bias_gradient = gradient_sum / len(pred_y)
    return bias_gradient, derivatives

bias_gradient,bias_deriv = gradient_b(predictions,y_train)


weight_deriv, weight_grad = gradient_w(w,b,x_train,y_train)


def update_parameter(gradient: float,old_value, learning_rate: float=0.01) -> float:
    new_w = old_value - (learning_rate)*(gradient)
    return new_w



epochs = 20
results = []
min_delta = 0.01

def train_step(x: list[int],w, b, actual: list[int]) -> tuple:
    initial_predictions = model(x,w,b)
    _, weight_grad = gradient_w(w,b,x,actual)
    bias_gradient,_ = gradient_b(initial_predictions,actual)
    new_weights = update_parameter(weight_grad, old_value=w)
    new_bias = update_parameter(bias_gradient,old_value=b)
    predictions = model(x,new_weights, new_bias)
    loss,MSE = mse(actual,predictions)
    
    return predictions, new_weights,new_bias, loss, MSE

best_loss = float('inf')
patience = 3
counter = 0
best_w = w
best_b = b
for i in range(epochs):
    _,w,b ,loss, MSE = train_step(x_train,w,b,y_train)
    if MSE > 10000:
        print('Divergence has been detected!')
        break
    if MSE < best_loss - min_delta:
        best_loss = MSE
        counter = 0
        best_w = w
        best_b = b
        print(counter)
    else:
        counter += 1
        if counter >= patience:
            print('Patience has run out')
            break
    print('best:', best_loss, 'MSE:', MSE)
    
    # print(f"{i},weight:, {w} ,bias:, {b}, loss:, {loss}, MSE: {MSE}")
w = best_w
b = best_b

# print('new predictions:', train_model(x))
