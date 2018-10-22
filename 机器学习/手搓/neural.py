# -*-coding:utf-8 -*-
import numpy
import scipy
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
        正态概率分布采样权重，分布中心设置为0.0，标准方差pow(),
        '''
        self.wih = numpy.random.normal(0.0,pow(self.hnodes,-0.5),(self.hnodes,self.inodes))
        self.who = numpy.random.normal(0.0,pow(self.onodes,-0.5),(self.onodes,self.hnodes))
        '''
        激活函数
        '''
        self.activation_function = lambda x:scipy.special.expit(x)
    def train(self):
        pass
    def query(self,inputs_list):
        '''
        转置矩阵
        '''
        inputs = numpy.array(inputs_list,nadmin=2).T
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

n.query([1.0,0.5,-0.5])

