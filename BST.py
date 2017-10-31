#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 15:43:00 2017

@author: alex
"""
import random

class Node(object):
    def __init__(self, data=None, left=None, right=None,
                 parent=None):
        self.data = data
        self.dcounter = 1
        self.left = left
        self.right = right
        self.parent = parent
    def getdata(self):
        return self.data
    def getchildL(self):
        return self.left
    def dcount(self):
        self.dcounter += 1
    def getchildR(self):
        return self.right
    def getparent(self):
        return self.parent
    def setparent(self, newparent):
        self.parent = newparent
    def setchildL(self, newchild):
        self.left = newchild
    def setchildR(self, newchild):
        self.right = newchild
        
class Tree(object):
    def __init__(self, start=None, current=None):
        self.start = start
        self.current = current
    def insert(self, dat):
        tnode = Node(dat)
        current = self.start
        if self.start == None:
            self.start = tnode
            current = self.start
        else:
            while tnode.getparent() == None:
                if tnode.getdata() < current.getdata():
                    if current.getchildL() == None:
                        current.setchildL(tnode)
                        tnode.setparent(current)
                    else:
                        current = current.getchildL()
                elif tnode.getdata() > current.getdata():
                    if current.getchildR() == None:
                        current.setchildR(tnode)
                        tnode.setparent(current)
                    else:
                        current = current.getchildR()
                elif current.getdata() == tnode.getdata():
                    current.dcount() 
                    
    def search(self, data):
        found = False
        current = self.start
        while found == False:
            self.current = current
            if current.getdata() == data:
                found = True
            elif data < current.getdata():
                if current.getchildL() == None:
                    break
                else:
                    current = current.getchildL()
            elif data > current.getdata():
                if current.getchildR() == None:
                    break
                else:
                    current = current.getchildR()
        if found == True:
            print ("found: "+str(current.getdata())+" "+str(current.dcounter)+
                   "x times in tree")
            return True
        else:
            print ("data not found")
    def delete(self, data): #if the item sought is the root then will not work.
        self.search(data) #find node to delete
        current = self.current
        delparent = current.getparent() #to be deleted node's parent
        delcurrent = current #to be deleted node
        if self.search(data) == True:
            if current.getchildL() == None and current.getchildR() == None:
                print ("leaf problem")
                if delparent.getchildL() == current:
                    delparent.setchildL(None)
                elif delparent.getchildR() == current:
                    delparent.setchildR(None)
            elif current.getchildL()== None or current.getchildR()==None:
                print ("single child problem")
                if current.getchildL() != None:
                    movedchild = current.getchildL()
                elif current.getchildR() != None:
                    movedchild = current.getchildR()
                if delparent.getchildL() == delcurrent:
                    delparent.setchildL(movedchild)
                elif delparent.getchildR() == delcurrent:
                    delparent.setchildR(movedchild)
            elif current.getchildL() != None and current.getchildR() != None:
                print ("double child problem")
                #searches for a leaf that is close but less than deleted node
                current = current.getchildL()
                while current.getchildL()!= None and current.getchildR()!=None:
                    current = current.getchildR()
                #deletes the leaf's parent's path to the leaf
                if current.getparent().getchildL() == current:
                    current.getparent().setchildL(None)
                elif current.getparent().getchildR() == current:
                    current.getparent().setchildR(None)
                #checks the paths of the deleted node's parent to confirm which
                #side it is and place the leaf
                if delparent.getchildL() == delcurrent:
                    delparent.setchildL(current)
                    current.setparent(delparent)
                    # these don't do what I want them tocurrent.setchildL(delcurrent.left)
                elif delparent.getchildR() == delcurrent:
                    delparent.setchildR(current)
                    current.setparent(delparent)
                    # nope but eventually current.setchildR(delcurrent.right)
            print ("Data: ("+str(data)+") found and removed")
        else:
            print ("data not found or deleted")
                       
    def __str__(self): #Credit to MIT 6.006 Algorithms course for ASCII artwork 
        if self.start is None: return '<empty tree>'
        def recurse(node):
            if node is None: return [], 0, 0
            label = str(node.data)
            left_lines, left_pos, left_width = recurse(node.left)
            right_lines, right_pos, right_width = recurse(node.right)
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            if (middle - len(label)) % 2 == 1 and node.parent is not None and \
               node is node.parent.left and len(label) < middle:
                label += '.'
            label = label.center(middle, '.')
            if label[0] == '.': label = ' ' + label[1:]
            if label[-1] == '.': label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle-2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
                [left_line + ' ' * (width - left_width - right_width) + 
                right_line
               for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width
        return '\n'.join(recurse(self.start) [0])                 

tre = Tree()
testdata = list(random.sample(range(30,101), 50))
print (testdata)

for dat in testdata:
    tre.insert(dat)
print (tre.__str__()) #ascii artwork of tree
print ("")
tre.search(76) #test functions
tre.delete(55) 
tre.search(55)
print (tre.__str__()) #prints tree again to confirm delete


