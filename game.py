#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter

number = 0  # 初始数值设置
num = -1  # 已经逃过一劫的次数
nmax = 1000  # 最大值
nmin = 0  # 最小值
#存放后端数据处理
def ebtnSubmit(event): #提交按钮设计
    global nmax,nmin,number,num
    if entry_a.get().isdigit(): #处理不是数字的情况
        val_a=int(float(entry_a.get()))
    else:
        lableval("请不要输入数字外的其他内容，请重新输入！(ノ=Д=)ノ┻━┻ ")
        entry_a.delete('0', 'end')
        return 0
    if num==-1:
        number=int(val_a)
        num+=1
        lableval("请从0-1000中进行一次试探╭(′▽`)╯")
        entry_a.delete('0', 'end')
    else:
        if val_a==number:
            num+=1
            BombResult() #踩中炸弹后的函数处理
        elif val_a<nmin or val_a>nmax:
            lableval("别捣乱，请在范围里猜！请再次从{}到{}之间试探 (ฅ´ω`ฅ)".format(nmin, nmax))
        elif val_a<number:
            nmin=val_a+1
            lableval("呼呼，比炸弹数字小，逃过一劫~（//▽//）请再次从{}到{}之间试探".format(nmin, nmax))
            entry_a.delete('0', 'end')
            num+=1
        else:
            nmax=val_a-1
            lableval("呼呼，比炸弹数字大，逃过一劫~（//▽//）请再次从{}到{}之间试探".format(nmin, nmax))
            entry_a.delete('0', 'end')
            num+=1

def BombResult(): #踩中炸弹的函数处理
    if num == 1:
        lableval('第一次就中，老倒霉蛋了，接受制裁吧！╮(๑• ₃•)╭')
    elif num<10:
        lableval('十次内中了，只能说配合的不是太好，接受惩罚吧！<(￣︶￣)>试探次数:{}'.format(num))
    else:
        lableval('害，十次后中，命也，该罚还是得罚！→_→试探次数:{}'.format(num))


def lableval(mytext): #标签函数
    lable_a.config(text=mytext)

def ebtnRestart(event):#重启按钮
    game()

#前端运行
root=tkinter.Tk(className='数字炸弹游戏')
root.geometry("400x90+550+300")
root.iconphoto(False, tkinter.PhotoImage(file='ak-12.png'))#默认图标
lable_a=tkinter.Label(root,width='80') #提示标签
entry_a=tkinter.Entry(root,width='40') #文本输入框
btnSubmit=tkinter.Button(root, text='提交') #提交按钮
btnRestart=tkinter.Button(root,text="重新开始")#再来一次按钮

#按键布局
lable_a.pack(side='top')
entry_a.pack(side='left')
btnSubmit.pack(side='left')
btnRestart.pack(side='left')

#绑定按键功能
entry_a.bind('<Return>',ebtnSubmit)
btnSubmit.bind('<Button-1>', ebtnSubmit)
btnRestart.bind('<Button-1>',ebtnRestart)

def game():
    global number,num,nmax,nmin
    entry_a.delete('0', 'end')
    number=0  # 初始数值设置
    num=-1  # 已经逃过一劫的次数
    nmax = 1000  # 最大值
    nmin = 0  # 最小值
    lableval('请输入你要放入的炸弹数字（0-1000） ( ‘-ωก̀ )')
    entry_a.focus_set()  # 焦点控制函数，运行后可直接输入文本

if __name__=='__main__':
    game()
    root.mainloop()