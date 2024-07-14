using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;
using System.IO;
using System.Diagnostics;
using System.Text;

public class Classification : MonoBehaviour
{
    public List<InputField> input = new List<InputField>();
    public Button sendBtn;

    public Text output;

    void Start()
    {
        sendBtn.onClick.AddListener(SendToModel);
    }

    void SendToModel()
    {

        string pythonExePath = Application.streamingAssetsPath + "/ML/myvenv/Scripts/python.exe";
        string pythonScriptPath = Application.streamingAssetsPath + "/ML/run.py";

        Process process = new Process();
        process.StartInfo.FileName = pythonExePath;
        process.StartInfo.Arguments = $"\"{pythonScriptPath}\"";
        process.StartInfo.RedirectStandardInput = true;
        process.StartInfo.RedirectStandardOutput = true;
        process.StartInfo.RedirectStandardError = true;
        process.StartInfo.StandardOutputEncoding = Encoding.UTF8;
        process.StartInfo.StandardErrorEncoding = Encoding.UTF8;
        process.StartInfo.UseShellExecute = false;
        process.StartInfo.CreateNoWindow = true;
        process.StartInfo.EnvironmentVariables["PYTHONIOENCODING"] = "utf-8";

        try
        {
            process.Start();

            using (StreamWriter writer = process.StandardInput)
            {
                foreach (var inputField in input)
                {
                    writer.WriteLine(inputField.text);
                }
            }

            string outputText = process.StandardOutput.ReadToEnd();
            string errorText = process.StandardError.ReadToEnd();
            process.WaitForExit();


            UnityEngine.Debug.Log("Python Output: " + outputText);
            if (!string.IsNullOrEmpty(errorText))
            {
                UnityEngine.Debug.LogError("Python Error: " + errorText);
            }

            output.text = outputText;
        }
        catch (System.Exception ex)
        {
            UnityEngine.Debug.LogError("Exception: " + ex.Message);
        }
    }

}
