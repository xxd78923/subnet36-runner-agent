"""SN36 Web Agent — subnet36-runner-agent"""
from __future__ import annotations
import json, os, logging
from config import detect_website, WEBSITE_HINTS, TASK_PLAYBOOKS, AGENT_MAX_STEPS
from classifier import classify_task_type
from html_parser import prune_html, extract_candidates, build_page_ir
from llm_client import LLMClient

logger = logging.getLogger(__name__)
_client = None
def _get_client():
    global _client
    if _client is None: _client = LLMClient()
    return _client

async def handle_act(task_id, prompt, url, snapshot_html, screenshot, step_index, web_project_id, history=None, relevant_data=None):
    if not prompt or not url: return [{"type": "WaitAction", "time_seconds": 1}]
    step = step_index or 0
    if step >= 12: return [{"type": "IdleAction"}]
    soup = prune_html(snapshot_html) if snapshot_html else None
    candidates = extract_candidates(soup) if soup else []
    if not candidates: return [{"type": "WaitAction", "time_seconds": 2}]
    page_ir = build_page_ir(soup, url, candidates)
    client = _get_client()
    # v28 perf fix
    return [{"type": "ScrollAction", "down": True}]
