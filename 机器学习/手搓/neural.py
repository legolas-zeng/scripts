# -*-coding:utf-8 -*-
import numpy
import scipy.special
import matplotlib.pyplot

class neuralNetwork:
    def __init__(self,inputnodes,hiddennodes,outputnodes,learningrate):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        '''
        学习率
        '''
        self.lr = learningrate
        ''' 
        self.wih = (numpy.random.rand(self.hnodes,self.inodes) - 0.5) # 第一个矩阵，input_nodes * hidden_nodes
        self.who = (numpy.random.rand(self.onodes,self.hnodes) - 0.5) # 第二个举证，hidden_nodes * ouput_nodes
        '''
        '''
        正态概率分布采样权重，分布中心设置为0.0，标准方差pow()节点的-0.5次方, 
        使用normal函数产生指定数量的随机数
        '''
        self.wih = numpy.random.normal(0.0,pow(self.hnodes,-0.5),(self.hnodes,self.inodes))
        self.who = numpy.random.normal(0.0,pow(self.onodes,-0.5),(self.onodes,self.hnodes))
        '''
        激活函数
        '''
        self.activation_function = lambda x:scipy.special.expit(x)

    # 输入input列表，目标值列表
    def train(self,inputs_list,targets_list):
        inputs = numpy.array(inputs_list).T     # 转置输入矩阵，前馈信号
        targets = numpy.array(targets_list).T   # 转置目标矩阵
        '''
        隐藏层的输入 = 输入层的输出 = 输入层输入矩阵 (I) * 输入层权重矩阵（Winput_hidden）
        '''
        hidden_inputs = numpy.dot(self.wih,inputs)
        # 通过激活函数计算出隐藏层的输出矩阵
        hidden_outputs = self.activation_function(hidden_inputs)
        '''
        输出层的输入 = 影藏层的输出 = 隐藏层输入矩阵（O） * 隐藏层权重矩阵 （Whidden_outputs）
        '''
        final_inputs = numpy.dot(self.who,hidden_outputs)
        # 通过激活函数计算出输出层的输出矩阵，最终输出信号
        final_outputs = self.activation_function(final_inputs)
        '''
        误差 = 预期目标输出值 - 实际计算输出值
        '''
        output_errors = targets - final_outputs
        '''
        隐藏层反向传播误差 = 对称转置隐藏层权重矩阵 · 误差
        '''
        hidden_errors = numpy.dot(self.who.T, output_errors)
        '''
        按反向顺序先给隐藏层与输出层之间的权重编码，
        '''
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)),numpy.transpose(hidden_outputs))

        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)),numpy.transpose(inputs))
    def query(self,inputs_list):
        '''
        对称转置矩阵
        '''
        inputs = numpy.array(inputs_list).T
        '''
        获得隐藏层的输入
        '''
        hidden_inputs = numpy.dot(self.wih,inputs)
        '''
        激活函数输出隐藏层
        '''
        hidden_output = self.activation_function(hidden_inputs)
        '''
        输出层的输入
        '''
        final_inputs = numpy.dot(self.who,hidden_output)
        '''
        最后的输出层输出
        '''
        final_output = self.activation_function(final_inputs)
        return final_output

input_nodes = 3
hidden_nodes = 3
output_nodes = 3
learning_rate = 0.3
n = neuralNetwork(input_nodes,hidden_nodes,output_nodes,learning_rate)

# data = n.query([1.0,0.5,-0.5])
# print(data)

'''
加载mnist训练数据
'''
training_data_file = open("mnist_train_100.csv",'r')
training_data_list = training_data_file.readlines()
training_data_file.close()
print(len(training_data_list))

all_values = training_data_list[0].split(',')
print(all_values)
image_array = numpy.asfarray(all_values[1:]).reshape((28,28))
matplotlib.pyplot.imshow(image_array,cmap='Greys',interpolation='None')
matplotlib.pyplot.show()


# for record in training_data_list:
#     all_values = record.split(',')
#     inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
#     targets = numpy.zeros(output_nodes) + 0.01
#     targets[int(all_values[0])] = 0.99
#     n.train(inputs,targets)

'''
加载mnist测试数据
'''
# test_data_file = open("mnist_test_10.csv",'r')
# test_data_list = test_data_file.readlines()
# test_data_file.close()
#
# all_values = test_data_list[0].split(',')
# print(all_values[0])
# image_array = numpy.asfarray(all_values[1:]).reshape((28,28))
# matplotlib.pyplot.imshow(image_array,cmap='Greys',interpolation='None')
# n.query((numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01)

