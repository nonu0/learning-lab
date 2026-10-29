import math

# x = [12,1,34]
# y_train = [20,40,60,80,150,120]
# x_train = [1,2,3,4,5,6]
# x_val = [5, 6]
# y_val = [100, 120]

x_train = [1, 2, 3, 4, 5, 6, 7, 8]
y_train = [22, 38, 63, 77, 117,180, 145, 160]

x_val = [1.5, 3.5, 5.5, 7.5]
y_val = [30, 69, 111, 151]

w = 10
b = 5

def model(x, w, b) -> list:
    preds = []
    for i in x:    
        y = w * i + b 
        preds.append(y)
    return preds

predictions = model(x_train,w,b)


def MSE(actual: list[int], pred: list[int]) -> tuple:
    losses = []
    # if len(actual) != len(pred):
    #     print('training and testing data are not of the same length')
    for i,j in zip(actual,pred):
        errors = (i - j) ** 2
        losses.append(errors)
    if actual is not None:
        se = sum(losses) / len(actual)
            
    return losses, se

# print('losses and MSE:', MSE(actual,predictions))


def MAE(actual, predictions):
    errors = []
    # if len(actual) != len(predictions):
    #     print('training and testing data are not of the same length')
    for i,j in zip(actual, predictions):
        y_pred = abs(i - j)
        errors.append(y_pred)
    sum_predictions = sum(errors)
    if actual is not None:
        mae = sum_predictions / len(actual)
    return errors, mae


actual = [10, 20, 30] 
target_y = [8, 24, 29]

print(MAE(actual, target_y))



def gradient_w(w: int, b: int, x: list[int], actual_y: list[int],lamda_reg) -> tuple:
    derivatives = []
    # if len(x) != len(actual_y):
    #     print('training and testing data are not of the same length')
    for x_i, y_i in zip(x, actual_y):
        der = -2*x_i*(y_i - w * x_i - b)
        derivatives.append(der)
    if x is not None:
        gradient = sum(derivatives) / len(x)
    if gradient is not None:
        regularized_gradient = gradient + 2 * lamda_reg * w
    return derivatives,gradient, regularized_gradient


def gradient_b(pred_y: list[int], actual_y: list[int]):
    derivatives = []
    # if len(pred_y) != len(actual_y):
    #     print('training and testing data are not of the same length')
    for y_i, j_y in zip(pred_y, actual_y):
        der = (j_y - y_i) * -2 
        derivatives.append(der)
    gradient_sum = sum(derivatives)
    if pred_y is not None:
        bias_gradient = gradient_sum / len(pred_y)
    return bias_gradient, derivatives

bias_gradient,bias_deriv = gradient_b(target_y,y_train)




def update_parameter(gradient: float,old_value, learning_rate: float) -> float:
    new_w = old_value - (learning_rate)*(gradient)
    return new_w



epochs = 100
results = []
min_delta = 0.1
learning_rate = 0.001

def train_step(x: list[int],w, b, actual: list[int]) -> tuple:
    initial_predictions = model(x,w,b)
    # print('target_y', initial_predictions)
    _, weight_grad, regularized_gradient = gradient_w(w,b,x,actual ,lamda_reg=2)
    bias_gradient,_ = gradient_b(initial_predictions,actual)
    new_weights = update_parameter(regularized_gradient, old_value=w, learning_rate=learning_rate)
    new_bias = update_parameter(bias_gradient,old_value=b, learning_rate=learning_rate)
    target_y = model(x,new_weights, new_bias)
    # print('Train target_y', initial_predictions)
    loss,mse = MSE(actual,target_y)
    
    return new_weights,new_bias, loss, mse, regularized_gradient

best_loss = float('inf')
patience = 3
counter = 0
best_w = w
best_b = b
for i in range(epochs):
    w,b ,train_loss, train_MSE, regularized_grad = train_step(x_train,w,b,y_train)
    validation_results = model(x_val,w,b)
    # print('validation predictions', validation_results)
    _,val_MSE = MSE(y_val, validation_results)
    if not math.isfinite(val_MSE) or not math.isfinite(train_MSE):
        print('Divergence has been detected!')
        break
    if val_MSE < best_loss - min_delta:
        best_loss = val_MSE
        counter = 0
        best_w = w
        best_b = b
        print(counter)
    else:
        counter += 1
        if counter >= patience:
            print('Patience has run out')
            break
    results.append(
        (f"Epoch: {i}",
        f"Learning Rate used: {learning_rate}",
        f"Training MSE:, {train_MSE}",
        f"Validation MSE:, {val_MSE}",
        f"Regularized gradient:, {regularized_grad}",
        # f"Best weight:, {best_w}",
        # f"Best bias:, {best_b}",
        )
    )
    print(results)
    
w = best_w
b = best_b

restored_preds = model(x_val,w,b)
_, restored_val_mse = MSE(y_val,restored_preds)


print("Restored weight:", w)
print("Restored bias:", b)
print("Best validation MSE:", best_loss)
print("Recalculated validation MSE:", restored_val_mse)
print("regularized Gradient:", regularized_grad)