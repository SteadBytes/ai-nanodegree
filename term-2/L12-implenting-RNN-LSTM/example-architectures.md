# Example RNN Architectures

<table class="index--table--2WHjQ index--table-striped--1ce0L">
<thead>
<tr>
<th style="text-align:center">Application</th>
<th style="text-align:center">Cell</th>
<th style="text-align:center">Layers</th>
<th style="text-align:center">Size</th>
<th style="text-align:center">Vocabulary</th>
<th style="text-align:center">Embedding Size</th>
<th style="text-align:center">Learning Rate</th>
<th style="text-align:center"></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">Speech Recognition (large vocabulary)</td>
<td style="text-align:center">LSTM</td>
<td style="text-align:center">5, 7</td>
<td style="text-align:center">600, 1000</td>
<td style="text-align:center">82K, 500K</td>
<td style="text-align:center">--</td>
<td style="text-align:center">--</td>
<td style="text-align:center"><a target="_blank" href="https://arxiv.org/abs/1610.09975">paper</a></td>
</tr>
<tr>
<td style="text-align:center">Speech Recognition</td>
<td style="text-align:center">LSTM</td>
<td style="text-align:center">1, 3, 5</td>
<td style="text-align:center">250</td>
<td style="text-align:center">--</td>
<td style="text-align:center">--</td>
<td style="text-align:center">0.001</td>
<td style="text-align:center"><a target="_blank" href="https://arxiv.org/abs/1303.5778">paper</a></td>
</tr>
<tr>
<td style="text-align:center">Machine Translation (seq2seq)</td>
<td style="text-align:center">LSTM</td>
<td style="text-align:center">4</td>
<td style="text-align:center">1000</td>
<td style="text-align:center">Source: 160K, Target: 80K</td>
<td style="text-align:center">1,000</td>
<td style="text-align:center">--</td>
<td style="text-align:center"><a target="_blank" href="https://arxiv.org/abs/1409.3215">paper</a></td>
</tr>
<tr>
<td style="text-align:center">Image Captioning</td>
<td style="text-align:center">LSTM</td>
<td style="text-align:center">--</td>
<td style="text-align:center">512</td>
<td style="text-align:center">--</td>
<td style="text-align:center">512</td>
<td style="text-align:center">(fixed)</td>
<td style="text-align:center"><a target="_blank" href="https://arxiv.org/abs/1411.4555">paper</a></td>
</tr>
<tr>
<td style="text-align:center">Image Generation</td>
<td style="text-align:center">LSTM</td>
<td style="text-align:center">--</td>
<td style="text-align:center">256, 400, 800</td>
<td style="text-align:center">--</td>
<td style="text-align:center">--</td>
<td style="text-align:center">--</td>
<td style="text-align:center"><a target="_blank" href="https://arxiv.org/abs/1502.04623">paper</a></td>
</tr>
<tr>
<td style="text-align:center">Question Answering</td>
<td style="text-align:center">LSTM</td>
<td style="text-align:center">2</td>
<td style="text-align:center">500</td>
<td style="text-align:center">--</td>
<td style="text-align:center">300</td>
<td style="text-align:center">--</td>
<td style="text-align:center"><a target="_blank" href="http://www.aclweb.org/anthology/P15-2116">pdf</a></td>
</tr>
<tr>
<td style="text-align:center">Text Summarization</td>
<td style="text-align:center">GRU</td>
<td style="text-align:center"></td>
<td style="text-align:center">200</td>
<td style="text-align:center">Source:  119K, Target:  68K</td>
<td style="text-align:center">100</td>
<td style="text-align:center">0.001</td>
<td style="text-align:center"><a target="_blank" href="https://pdfs.semanticscholar.org/3fbc/45152f20403266b02c4c2adab26fb367522d.pdf">pdf</a></td>
</tr>
</tbody>
</table>
