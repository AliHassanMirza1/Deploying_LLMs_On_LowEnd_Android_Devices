sshpass -p ' ' ssh HP@192.168.18.8 'cmd /c "echo log.txt > D:\Academics\LLM\Research\output.txt"' && ollama run llama3.2:1b-instruct-q2_K "Explain the water cycle in simple terms" --verbose && sshpass -p ' ' ssh HP@192.168.18.8 'cmd /c "echo exit > D:\Academics\LLM\Research\output.txt"'