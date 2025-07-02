
import random

class AI:
    def choose_action(self, snake, food):
        return random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])

    def action_to_direction(self, action, current_direction):
        if action == 'UP':
            return (0, -10)
        elif action == 'DOWN':
            return (0, 10)
        elif action == 'LEFT':
            return (-10, 0)
        elif action == 'RIGHT':
            return (10, 0)
        return current_direction

    def generate_food(self, width, height, snake):
        while True:
            new_food = (random.randint(0, (width-10)//10)*10, random.randint(0, (height-10)//10)*10)
            if new_food not in snake:
                return new_food

    def train(self):
        pass
