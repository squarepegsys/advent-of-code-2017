
from nose.tools import assert_equals

def test_register():

    cpu = CPU()

    cpu.next_instruction("b inc 5 if a > 1")
    
    assert_equals(cpu.registers["a"],0)
    assert_equals(cpu.registers["b"],0)

    cpu.next_instruction("a inc 1 if b < 5")

    assert_equals(cpu.registers["a"],1)
    assert_equals(cpu.registers["b"],0)

    
    cpu.next_instruction("c dec -10 if a >= 1")
    assert_equals(cpu.registers["a"],1)
    assert_equals(cpu.registers["b"],0)
    assert_equals(cpu.registers["c"],10)


    cpu.next_instruction("c inc -20 if c == 10")
    assert_equals(cpu.registers["a"],1)
    assert_equals(cpu.registers["b"],0)
    assert_equals(cpu.registers["c"],-10)

    assert_equals(cpu.max_value(),1)

    assert_equals(cpu.highest_held,10)
class CPU:

    registers={}
    highest_held=-1000000

    def next_instruction(self,instruction):

        operation,condition = instruction.split(" if ")

        register,operation,value = operation.split(" ")

        if register not in self.registers.keys():
            self.registers[register]=0

        if self.isTrue(condition):
            getattr(self,operation)(register,value)

            if (self.registers[register]>self.highest_held):
                self.highest_held=self.registers[register]

    def isTrue(self,condition):

        register,tester,value = condition.split(" ")

        reg_value = self.registers.get(register,0)
        
        if register not in self.registers.keys():
            self.registers[register]=0

        if tester=="<":
            return reg_value<int(value)

        if tester==">":
            return reg_value>int(value)

        if tester==">=":
            return reg_value>=int(value)

        if tester=="<=":
            return reg_value<=int(value)


        if tester=="==":
            return reg_value==int(value)

        if tester=="!=":
            return reg_value!=int(value)


        raise Exception("Unknown operation %s" %tester)

        

    def inc(self,register,value):
        self.registers[register]+=int(value)


    def dec(self,register,value):
        
        self.registers[register]-=int(value)

    def max_value(self):

        return max(self.registers.values())


if __name__=='__main__':

    cpu = CPU()

    with open("input.txt") as input_fp:

        for line in input_fp.readlines():
            cpu.next_instruction(line.strip())

    print(cpu.max_value())

    print(cpu.highest_held)
