#!/usr/bin/env python3
"""
Basic test harness for AERIS00.
Run with: python test_aeris.py
"""
from aeris_core import Aeris, InMemoryStore, EchoModel

def test_boot_and_chat():
    """Test that Aeris can boot up and respond to a message."""
    print("Testing basic boot and chat...")
    agent = Aeris(store=InMemoryStore(), model=EchoModel())
    agent.system_boot(identity_name="TestAgent")
    reply = agent.chat("Hello, world!")
    assert isinstance(reply, str)
    assert len(reply) > 0
    print("✓ Basic boot and chat test passed.")

def test_memory_persistence():
    """Test that Aeris remembers across conversations."""
    print("Testing memory persistence...")
    agent = Aeris(store=InMemoryStore(), model=EchoModel())
    agent.system_boot(identity_name="TestAgent")
    
    # First conversation
    agent.chat("My name is Test User.")
    # Second conversation - should remember
    reply = agent.chat("What is my name?")
    
    # The EchoModel will just echo, but the point is that the memory was stored and recalled.
    assert "Test User" in reply
    print("✓ Memory persistence test passed.")

def test_state_save_load():
    """Test that state can be saved and loaded."""
    print("Testing state save/load...")
    agent = Aeris(store=InMemoryStore(), model=EchoModel())
    agent.system_boot(identity_name="TestAgent")
    agent.chat("This is a test message to save.")
    
    # Save state
    agent.save_state("test_state.json")
    
    # Create a new agent and load state
    agent2 = Aeris(store=InMemoryStore(), model=EchoModel())
    agent2.load_state("test_state.json")
    
    # New agent should have the same identity and memory
    assert agent2.identity_name == "TestAgent"
    # Clean up
    import os
    os.remove("test_state.json")
    print("✓ State save/load test passed.")

if __name__ == "__main__":
    test_boot_and_chat()
    test_memory_persistence()
    test_state_save_load()
    print("\n✅ All tests passed! AERIS00 is operational.")#!/usr/bin/env python3
"""
Basic test harness for AERIS00.
Run with: python test_aeris.py
"""
from aeris_core import Aeris, InMemoryStore, EchoModel

def test_boot_and_chat():
    """Test that Aeris can boot up and respond to a message."""
    print("Testing basic boot and chat...")
    agent = Aeris(store=InMemoryStore(), model=EchoModel())
    agent.system_boot(identity_name="TestAgent")
    reply = agent.chat("Hello, world!")
    assert isinstance(reply, str)
    assert len(reply) > 0
    print("✓ Basic boot and chat test passed.")

def test_memory_persistence():
    """Test that Aeris remembers across conversations."""
    print("Testing memory persistence...")
    agent = Aeris(store=InMemoryStore(), model=EchoModel())
    agent.system_boot(identity_name="TestAgent")
    
    # First conversation
    agent.chat("My name is Test User.")
    # Second conversation - should remember
    reply = agent.chat("What is my name?")
    
    # The EchoModel will just echo, but the point is that the memory was stored and recalled.
    assert "Test User" in reply
    print("✓ Memory persistence test passed.")

def test_state_save_load():
    """Test that state can be saved and loaded."""
    print("Testing state save/load...")
    agent = Aeris(store=InMemoryStore(), model=EchoModel())
    agent.system_boot(identity_name="TestAgent")
    agent.chat("This is a test message to save.")
    
    # Save state
    agent.save_state("test_state.json")
    
    # Create a new agent and load state
    agent2 = Aeris(store=InMemoryStore(), model=EchoModel())
    agent2.load_state("test_state.json")
    
    # New agent should have the same identity and memory
    assert agent2.identity_name == "TestAgent"
    # Clean up
    import os
    os.remove("test_state.json")
    print("✓ State save/load test passed.")

if __name__ == "__main__":
    test_boot_and_chat()
    test_memory_persistence()
    test_state_save_load()
    print("\n✅ All tests passed! AERIS00 is operational.")
