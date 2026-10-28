# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

#Test commit

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, ClockCycles, Timer

@cocotb.test()
async def test_project(dut):
    dut._log.info("Starting 8-bit Counter Test")
    
    # Initialize signals
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    
    # Start a 10 MHz clock (100ns period)
    clock = Clock(dut.clk, 100, units="ns")
    cocotb.start_soon(clock.start())
    
    # Apply active-low reset
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1
    await RisingEdge(dut.clk)
    await Timer(1, units="ns")
    dut._log.info("Reset released")
    
    # Test 1: Hold when enable is 0
    dut.ui_in.value = 0b00
    await ClockCycles(dut.clk, 3)
    assert int(dut.uo_out.value) == 0, f"Counter should hold at 0, got {dut.uo_out.value}"
    
    # Test 2: Count when enable is 1 (ui[0] = 1)
    dut.ui_in.value = 0b01
    for expected_val in range(1, 10):
        await RisingEdge(dut.clk)
        await Timer(1, units="ns")
        assert int(dut.uo_out.value) == expected_val, f"Expected {expected_val}, got {dut.uo_out.value}"
        
    # Test 3: Synchronous Reset (ui[1] = 1)
    dut.ui_in.value = 0b11 
    await RisingEdge(dut.clk)
    await Timer(1, units="ns")
    assert int(dut.uo_out.value) == 0, f"Synchronous reset failed, got {dut.uo_out.value}"
    
    # Test 4: Disable and hold value
    dut.ui_in.value = 0b00 
    held_val = int(dut.uo_out.value)
    await ClockCycles(dut.clk, 3)
    assert int(dut.uo_out.value) == held_val, f"Counter should hold value {held_val}, got {dut.uo_out.value}"
    
    dut._log.info("All counter tests passed successfully!")
