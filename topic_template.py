# coding: utf8
from __future__ import unicode_literals


# setting explicit height and max-width: none on the SVG is required for
# Jupyter to render it properly in a cell

TPL_ONT_SVG = """
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" id="l1{id}" class="displacy" width="{width}" height="{height}" style="max-width: none; height: {height}px; color: {color}; background: {bg}; font-family: {font}">{content}
        </svg>
"""

TPL_LIN_VER = """
            <line stroke="#000" id="svg_3" x1={x} x2={x} y1={y1} y2={y2} fill="none"/>
"""


TPL_TOP_BOX = """
            <g class="displacy-arrow">
            <rect id="svg_4" height={height} rx="15" ry="40" width={width} x={x} y={y} stroke="#000" fill="#fff"/>
            <text class="displacy-token" fill="currentColor" text-anchor="middle">
                <tspan class="displacy-eword" fill="{tcolor}" font-size=1.4em x="{x1}" y="{y1}">{etext}</tspan>
                <tspan class="displacy-aword" fill="{tcolor}" font-size=1.4em x="{x1}" y="{y2}">{atext}</tspan>
            </text>
            </g>
"""



TPL_LIN_HOR = """
            <line id="svg_5" x1={x1}  y1={y1} x2={x2} y2={y2} stroke="#000" fill="none"/>
"""



TPL_PAGE = """
<!DOCTYPE html>
<html>
    <head>
        <title>القران الكريم</title>
    </head>

    <body style="font-size: 16px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; padding: 4rem 2rem;">{content}</body>
</html>
"""

TPL_STORY =  """
              <div align="right"
    style='margin-top:0in;margin-right:0in;margin-bottom:8.0pt;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;'>
    <table dir="rtl" style="border: none;border-collapse:collapse;">
        <tbody>
            <tr>
                <td style="width: 467.5pt;padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL"
                        style='margin-top:12.0pt;margin-right:  0in;margin-bottom:0in;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:center;line-height:normal;'>
                        <strong><span
                                style='font-size:35px;font-family:"Noto Naskh Arabic";color:#1F4E79;'>{title}</span></strong>
                    </p>
                </td>
            </tr>
                {story}
            <tr>
                <td style="width: 467.5pt;background: rgb(242, 242, 242);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL"
                        style='margin-top:12.0pt;margin-right:0in;margin-bottom:0in;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:right;line-height:normal;'>
                        <strong><span style='font-size:29px;font-family:"Noto Naskh Arabic";color:#1F4E79;'>العبرة من
                                القصة:</span></strong>
                    </p>
                </td>
            </tr>
            {moral}
            <tr>
                <td style="width: 467.5pt;background: rgb(242, 242, 242);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL"
                        style='margin-top:12.0pt;margin-right:0in;margin-bottom:0in;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:right;line-height:normal;'>
                        <strong><span style='font-size:29px;font-family:"Noto Naskh Arabic";color:#1F4E79;'>سؤال
                                للطفل:</span></strong>
                    </p>
                </td>
            </tr>
            {question}
            <tr>
                <td style="width: 467.5pt;background: rgb(242, 242, 242);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL"
                        style='margin-top:12.0pt;margin-right:0in;margin-bottom:0in;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:right;line-height:normal;'>
                        <strong><span
                                style='font-size:29px;font-family:"Noto Naskh Arabic";color:#1F4E79;'>الجواب:</span></strong>
                    </p>
                </td>
            </tr>
            {answer}
        </tbody>
    </table>
</div>
"""
    
TPL_PRAG = """            <tr>
                <td style="width: 467.5pt;background: rgb(242, 242, 242);padding: 0in 5.4pt;vertical-align: top;">
                    <p dir="RTL"
                        style='margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:0in;font-size:11.0pt;font-family:"Calibri",sans-serif;text-align:justify;line-height:normal;'>
                        <strong><span
                                style='font-size:29px;font-family:"Noto Naskh Arabic";color:#0070C0;'>{kids}</span></strong>
                    </p>
                </td>
            </tr>
            """
