path = debug.getinfo(1).source:match("@?(.*/)")

-- Register all Toolbar actions and intialize all UI stuff
function initUi()
    local venvDir = path .. "venv"
    os.execute("python3 -m venv " .. venvDir);
    if operatingSystem == "Windows" then
      local activateScript = venvDir .. '/Scripts/activate';
    else
      local activateScript = '. ' .. venvDir .. '/bin/activate';
    end

    os.execute(activateScript);

    os.execute("pip install -r " .. path .. "requirements.txt");

    ref = app.registerUi({["menu"] = "MathCopilot", ["callback"] = "run", ["accelerator"] = "<Shift><Alt>F1"});
  end
  
  -- Callback if the menu item is executed
  function run()
    os.execute("maim -s > " .. path .. "data/curr.png")
    local python_cmd = "python3 " .. path .. "main.py " .. path
    os.execute(python_cmd)
  end
  