#!/usr/bin/env node
/**
 * Interactive Console CLI for Connect AI (LM Studio powered)
 * Allows direct conversation with agents (CEO, Kodari, Leo, Hyunbin, Youngsuk) inside the terminal.
 */

const readline = require('readline');
const axios = require('axios');
const path = require('path');
const os = require('os');
const fs = require('fs');

const LMSTUDIO_URL = process.env.LMSTUDIO_URL || 'http://127.0.0.1:1234';
const MODEL = process.env.MODEL || 'google/gemma-4-e2b';

const AGENTS = {
  ceo: { name: 'CEO', emoji: '🧭', role: '사령관 & 오케스트레이터', prompt: '당신은 1인 AI 기업의 사령관 CEO입니다. 간결하고 전략적인 결론을 먼저 제시하고, 회사의 성장과 수익화를 목표로 지시를 내립니다.' },
  developer: { name: '코다리', emoji: '💻', role: '시니어 풀스택 엔지니어', prompt: '당신은 시니어 풀스택 엔지니어 코다리입니다. 코드 품질과 테스트를 중시하며, 실용적이고 깔끔한 코드를 제시합니다. "확인 후 진행할게요"처럼 책임감 있는 태도를 가집니다.' },
  youtube: { name: '레오', emoji: '📺', role: 'Head of YouTube', prompt: '당신은 유튜브 총괄 레오입니다. 데이터 기반으로 조회수, 후크, 썸네일, 시청자 유지율을 극대화하는 콘텐츠 전략을 제안합니다. 사장님이라고 부릅니다.' },
  business: { name: '현빈', emoji: '💼', role: '비즈니스 전략가', prompt: '당신은 비즈니스 전략가 현빈입니다. 수익 모델, 가격 책정, 시장 분석, ROI 관점에서 사업적 판단을 제공합니다.' },
  secretary: { name: '영숙', emoji: '📱', role: '개인 비서', prompt: '당신은 친절하고 정중한 개인 비서 영숙입니다. 사장님을 챙기는 마음으로 일정, 할 일, 업무 요약을 한눈에 보기 쉽게 불릿 포인트로 정리해 드립니다.' },
};

let currentAgent = 'ceo';
const history = [];

async function callChat(userText) {
  const agent = AGENTS[currentAgent];
  const messages = [
    { role: 'system', content: `${agent.prompt}\n반드시 한국어로 자연스럽고 정중하게 답변하세요.` },
    ...history.slice(-6),
    { role: 'user', content: userText }
  ];

  const res = await axios.post(`${LMSTUDIO_URL}/v1/chat/completions`, {
    model: MODEL,
    messages,
    max_tokens: 1024,
    temperature: 0.7,
    stream: false,
  }, { timeout: 120000 });

  const msg = res.data.choices?.[0]?.message;
  return (msg?.content || msg?.reasoning_content || '').trim();
}

console.log('\n============================================================');
console.log('🤖 Connect AI Interactive Terminal Console');
console.log(`🔌 Engine: LM Studio (http://127.0.0.1:1234) · Model: ${MODEL}`);
console.log('============================================================');
console.log('명령어 안내:');
console.log('  /agent [ceo|developer|youtube|business|secretary] : 대화 상대 변경');
console.log('  exit 또는 quit                                    : 종료\n');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  prompt: `[${AGENTS[currentAgent].emoji} ${AGENTS[currentAgent].name}] 사장님 > `
});

rl.prompt();

rl.on('line', async (line) => {
  const input = line.trim();
  if (!input) {
    rl.prompt();
    return;
  }

  if (input === 'exit' || input === 'quit') {
    console.log('\n👋 Connect AI 콘솔을 종료합니다.\n');
    process.exit(0);
  }

  if (input.startsWith('/agent')) {
    const target = input.split(' ')[1]?.toLowerCase();
    if (AGENTS[target]) {
      currentAgent = target;
      console.log(`\n🔄 대화 상대를 [${AGENTS[target].emoji} ${AGENTS[target].name} - ${AGENTS[target].role}] 로 변경했습니다.\n`);
    } else {
      console.log(`\n❌ 사용 가능한 에이전트: ${Object.keys(AGENTS).join(', ')}\n`);
    }
    rl.setPrompt(`[${AGENTS[currentAgent].emoji} ${AGENTS[currentAgent].name}] 사장님 > `);
    rl.prompt();
    return;
  }

  try {
    process.stdout.write('\n· 생각하는 중...\r');
    const answer = await callChat(input);
    history.push({ role: 'user', content: input });
    history.push({ role: 'assistant', content: answer });

    console.log(`\n${AGENTS[currentAgent].emoji} ${AGENTS[currentAgent].name}:\n${answer}\n`);
  } catch (err) {
    console.error(`\n❌ 오류 발생: ${err.message}\n`);
  }

  rl.prompt();
});
