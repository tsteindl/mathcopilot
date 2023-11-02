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

    png_file = "curr"

    ref = app.registerUi({["menu"] = "MathCopilot", ["callback"] = "run", ["accelerator"] = "<Shift><Alt>F1"});
  end
  
  -- Callback if the menu item is executed
  function run()
    local pngPath = path .. "data/" .. png_file .. ".png";
    local tex_file_path = path .. "data/" .. png_file .. ".tex"
    -- local success, err_msg = os.remove(tex_file_path) --remove existing tex file
    -- if success then
      -- print("File deleted successfully.")
    -- else
      -- print("Failed to delete the file:", err_msg)
    -- end
    os.execute("maim -s > " .. pngPath)
    os.execute("mpx convert " .. pngPath .. " " .. tex_file_path)
    local python_cmd = "python3 " .. path .. "main.py " .. path .. " " .. png_file
    -- os.execute(python_cmd)
    local pipe = io.popen(python_cmd, "r")
    local return_value = pipe:read("*a")
    pipe:close()

    app.openDialog(return_value, {"Ok"});
  end
  