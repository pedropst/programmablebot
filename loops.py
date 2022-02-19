from calendar import c


class Loops():
    def __init__(self, start, end, count, commands, parent=None):
        print('entrou construtor loop')
        print(start)
        print(end)
        self.start = start
        self.end = end
        self.children = []
        self.parent = parent
        self.commands = commands
        self.real_commands = []
        self.expanded_commands = []
        self.count = count
        self.check_inner_loop()
        self.get_commands()
        self.get_expanded_commands()

    def check_inner_loop(self):
        print('entrou inner check')
        for i in range(self.start + 1, self.end):
            if self.commands[i][0].get() == 'START LOOP':
                count = int(self.commands[i][1].get().split(',')[1])
                j = 1
                while 1:
                    if j+i >= len(self.commands[i]) or (self.commands[i + j][0].get() != 'END LOOP' and self.commands[i + j][1].get() == self.commands[i][1].get().split(',')[0]):
                        break
                    j += 1
                inner_commands = self.commands[i:i+j]
                print(len(inner_commands))
                c = Loops(i, i+j, count, self.commands)
                print('criou filho')
                self.children.append(c)
    
    def get_commands(self):
        print('entrou get commands')
        commands = []
        points = []

        x = 0
        for i in range(1, len(self.commands)-1):
            if self.commands[i][0].get() != 'START LOOP':
                commands.append(self.commands[i])
            else:
                i += len(self.children[x].commands)
                for j in range(0, len(self.children[x].expanded_commands)):
                    commands.append(self.children[x].expanded_commands[j])
                x += 1
                
        # for i in range(self.start, self.end + 1):
        #     points.append(i)
        # children_commands = []
        # for i in self.children:
        #     for j in range(self.children[i].start, self.children[i].end + 1):
        #         try:
        #             points.remove(j)
        #         except ValueError:
        #             pass
        #     children_commands.append(self.children[i].expanded_commands)
        # for i in range(0, len(points)):
        #     commands.append(self.commands[points[i]])
        
        self.real_commands = commands

    def get_expanded_commands(self):
        print('entrou get expanded')
        for _ in range(0, self.count):
            for i in range(0, len(self.real_commands)):
                self.expanded_commands.append(self.real_commands[i])