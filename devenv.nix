{ pkgs, lib, config, inputs, ... }:
{
  env.GREET = "devenv";

  packages = [
    pkgs.git
    pkgs.ollama-rocm
    pkgs.uv
  ];

  scripts.hello.exec = "echo hello from $GREET";

  enterShell = ''
    hello
    git --version
  '';

  enterTest = ''
    echo "Running tests"
    git --version | grep "2.42.0"
  '';
  languages.python = {
    enable = true;
    venv.enable = true;
    venv.requirements = ''
      ollama
      crewai
      crewai-tools
      unstructured
      langchain-community
      Jinja2>=3.1.2
      click>=7.0
      duckduckgo-search
    '';
    uv.enable = true;
  };
  dotenv.enable = true;
}
