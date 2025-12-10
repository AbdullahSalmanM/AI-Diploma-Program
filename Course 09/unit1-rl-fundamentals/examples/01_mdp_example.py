"""
Unit 1 - Example 1: Markov Decision Process (MDP)
الوحدة 1 - مثال 1: عملية القرار الماركوفية

This example demonstrates:
1. MDP structure
2. States, actions, and rewards
3. Transition probabilities
4. Policy representation
"""

print("=" * 60)
print("Example 1: Markov Decision Process (MDP)")
print("مثال 1: عملية القرار الماركوفية")
print("=" * 60)

# Simple MDP: Grid World
# MDP بسيط: عالم الشبكة
print("\n1. MDP Components")
print("مكونات MDP")
print("-" * 60)

# States: positions in a 3x3 grid
# الحالات: المواضع في شبكة 3x3
states = {
    (0, 0): "Start",
    (0, 1): "State 1",
    (0, 2): "State 2",
    (1, 0): "State 3",
    (1, 1): "State 4",
    (1, 2): "State 5",
    (2, 0): "State 6",
    (2, 1): "State 7",
    (2, 2): "Goal"
}

# Actions: up, down, left, right
# الإجراءات: أعلى، أسفل، يسار، يمين
actions = ['up', 'down', 'left', 'right']

# Rewards: reward for each state
# المكافآت: مكافأة لكل حالة
rewards = {
    (0, 0): -0.1,
    (0, 1): -0.1,
    (0, 2): -0.1,
    (1, 0): -0.1,
    (1, 1): -0.1,
    (1, 2): -0.1,
    (2, 0): -0.1,
    (2, 1): -0.1,
    (2, 2): 10.0  # Goal state
}

print("\nStates:")
for state, description in states.items():
    reward = rewards[state]
    print(f"  {state}: {description} (reward: {reward})")

print(f"\nActions: {actions}")

# Transition probabilities (simplified)
# احتمالات الانتقال (مبسطة)
def get_next_state(state, action):
    """
    Get next state after taking action (simplified).
    الحصول على الحالة التالية بعد اتخاذ الإجراء (مبسط).
    """
    row, col = state
    
    if action == 'up' and row > 0:
        return (row - 1, col)
    elif action == 'down' and row < 2:
        return (row + 1, col)
    elif action == 'left' and col > 0:
        return (row, col - 1)
    elif action == 'right' and col < 2:
        return (row, col + 1)
    
    return state  # Stay in same state if action invalid

# Example: Starting from (0,0) and moving right
print("\n" + "=" * 60)
print("2. Example Transition")
print("مثال على الانتقال")
print("=" * 60)

start_state = (0, 0)
action_taken = 'right'
next_state = get_next_state(start_state, action_taken)

print(f"\nStart state: {start_state} ({states[start_state]})")
print(f"Action: {action_taken}")
print(f"Next state: {next_state} ({states[next_state]})")
print(f"Reward received: {rewards[next_state]}")

# Policy: mapping from states to actions
# السياسة: تعيين من الحالات إلى الإجراءات
print("\n" + "=" * 60)
print("3. Policy Example")
print("مثال على السياسة")
print("=" * 60)

# Simple policy: always move towards goal
# سياسة بسيطة: التحرك دائماً نحو الهدف
policy = {
    (0, 0): 'right',
    (0, 1): 'right',
    (0, 2): 'down',
    (1, 0): 'right',
    (1, 1): 'right',
    (1, 2): 'down',
    (2, 0): 'right',
    (2, 1): 'right',
    (2, 2): None  # Goal state, no action needed
}

print("\nPolicy (state -> action):")
for state, action in policy.items():
    if action:
        print(f"  {state}: {action}")

print("\n" + "=" * 60)
print("Example completed successfully!")
print("تم إكمال المثال بنجاح!")
print("=" * 60)

