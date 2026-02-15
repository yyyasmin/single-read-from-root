import { useState, useEffect } from 'react'

const API_BASE = (import.meta.env.VITE_API_URL || '').replace(/\/$/, '') + '/api'

function Menu({ onChoose }) {
  return (
    <>
      <h1>לקרוא מן השורש</h1>
      <p className="instruction">בחר משחק והתחל לשחק!</p>
      <div className="menu">
        <button className="menu-btn logical" onClick={() => onChoose('logical')}>
          משפט הגיוני? (בחר מהזוג)
        </button>
        <button className="menu-btn verbs" onClick={() => onChoose('verbs')}>
          התאמת פועל – הבנות והבנים
        </button>
        <button className="menu-btn yesno" onClick={() => onChoose('yesno3')}>
          כן או לא? (צירוף-סגול)
        </button>
        <button className="menu-btn yesno" onClick={() => onChoose('yesno6')}>
          כן או לא? (קמץ-פתח)
        </button>
        <button className="menu-btn logical" onClick={() => onChoose('logical5')}>
          איזה משפט הגיוני? (חיריק)
        </button>
        <button className="menu-btn completion" onClick={() => onChoose('completion')}>
          השלם את המשפט
        </button>
        <button className="menu-btn transform" onClick={() => onChoose('transform')}>
          קראו והשלימו (החלפת גוף)
        </button>
        <button className="menu-btn root" onClick={() => onChoose('root')}>
          מילה מהשורש
        </button>
        <button className="menu-btn pyramid" onClick={() => onChoose('pyramid')}>
          קריאת פירמידה
        </button>
      </div>
    </>
  )
}

const PYRAMID_LEVELS = [
  { id: 'patach', label: 'פתח' },
  { id: 'kamatz', label: 'קמץ' },
  { id: 'chirik', label: 'חיריק' },
  { id: 'cholam', label: 'חולם' },
  { id: 'tsere_segol', label: 'צירה, סגול' },
  { id: 'mixed', label: 'משולב' },
  { id: 'word_to_sentence', label: 'מילה למשפט (5 מילים)' },
]

function PyramidLevelMenu({ onChooseLevel, onBack }) {
  return (
    <>
      <button className="back-btn" onClick={onBack}>← חזרה</button>
      <h2>קריאת פירמידה</h2>
      <p className="instruction">בחר דף – מהקל אל הקשה</p>
      <div className="menu">
        {PYRAMID_LEVELS.map((lev) => (
          <button
            key={lev.id}
            className="menu-btn pyramid"
            onClick={() => onChooseLevel(lev.id)}
          >
            {lev.label}
          </button>
        ))}
      </div>
    </>
  )
}

function PyramidGame({ tasks, levelLabel, onBack }) {
  const [index, setIndex] = useState(0)
  const [chosen, setChosen] = useState(null)
  const [score, setScore] = useState(0)
  const [showFeedback, setShowFeedback] = useState(false)
  const task = tasks[index]
  const isLast = index === tasks.length - 1
  const isChoose = task && task.mode === 'choose'
  const options = isChoose && task.options ? [...task.options].sort(() => Math.random() - 0.5) : []

  const handleChoose = (word) => {
    if (chosen !== null) return
    setChosen(word)
    const correctWord = task.options[task.correct - 1]
    if (word === correctWord) setScore((s) => s + 1)
    setShowFeedback(true)
  }

  const handleNext = () => {
    if (isLast) return
    setIndex((i) => i + 1)
    setChosen(null)
    setShowFeedback(false)
  }

  const handleFinish = () => {
    setIndex(0)
    setChosen(null)
    setShowFeedback(false)
    setScore(0)
    onBack()
  }

  if (!task) return null
  const correctChosen = isChoose ? chosen === task.options[task.correct - 1] : true

  return (
    <>
      <button className="back-btn" onClick={onBack}>← חזרה</button>
      <h2>קריאת פירמידה – {levelLabel}</h2>
      <p className="progress">תרגיל {index + 1} מתוך {tasks.length}</p>
      <div className={`task-card pyramid-card ${levelLabel.includes('מילה למשפט') ? 'pyramid-sentence' : ''}`}>
        <div className="pyramid-rows">
          {task.rows.map((row, i) => (
            <div key={i} className="pyramid-row">{row}</div>
          ))}
        </div>
        {isChoose ? (
          <>
            <p className="instruction">איזו מילה קראת?</p>
            <div className="options">
              {options.map((word) => {
                const correctWord = task.options[task.correct - 1]
                const showCorrect = chosen !== null && word === correctWord
                const showWrong = chosen !== null && chosen === word && word !== correctWord
                return (
                  <button
                    key={word}
                    className={`option-btn ${showCorrect ? 'correct' : showWrong ? 'wrong' : ''}`}
                    onClick={() => handleChoose(word)}
                    disabled={chosen !== null}
                  >
                    {word}
                  </button>
                )
              })}
            </div>
            {showFeedback && (
              <p className={`feedback ${correctChosen ? 'good' : 'bad'}`}>
                {correctChosen ? 'כל הכבוד! ✓' : 'לא הפעם. הנכון: ' + task.options[task.correct - 1]}
              </p>
            )}
          </>
        ) : (
          <p className="pyramid-read-hint">קרא את הפירמידה ואז לחץ הבא</p>
        )}
        {(!isChoose || showFeedback) && (
          isLast ? (
            <button className="next-btn" onClick={handleFinish}>סיום וחזרה לדפים</button>
          ) : (
            <button className="next-btn" onClick={handleNext}>הבא →</button>
          )
        )}
      </div>
      {isLast && showFeedback && (
        <p className="summary"><strong>ניקוד: {score} מתוך {tasks.length}</strong></p>
      )}
    </>
  )
}

function LogicalGame({ tasks, onBack, title }) {
  const [index, setIndex] = useState(0)
  const [chosen, setChosen] = useState(null)
  const [score, setScore] = useState(0)
  const [showFeedback, setShowFeedback] = useState(false)
  const task = tasks[index]
  const isLast = index === tasks.length - 1

  const handleChoose = (optionNum) => {
    if (chosen !== null) return
    setChosen(optionNum)
    if (optionNum === task.correct) setScore((s) => s + 1)
    setShowFeedback(true)
  }

  const handleNext = () => {
    if (isLast) return
    setIndex((i) => i + 1)
    setChosen(null)
    setShowFeedback(false)
  }

  const handleFinish = () => {
    setIndex(0)
    setChosen(null)
    setShowFeedback(false)
    setScore(0)
    onBack()
  }

  if (!task) return null
  const correctChosen = chosen === task.correct

  return (
    <>
      <button className="back-btn" onClick={onBack}>← חזרה</button>
      <h2>{title || 'סמנו את המשפט ההגיוני'}</h2>
      <p className="progress">שאלה {index + 1} מתוך {tasks.length}</p>
      <div className="task-card">
        <div className="options">
          <button
            className={`option-btn ${chosen === 1 ? (task.correct === 1 ? 'correct' : 'wrong') : ''}`}
            onClick={() => handleChoose(1)}
            disabled={chosen !== null}
          >
            {task.option1}
          </button>
          <button
            className={`option-btn ${chosen === 2 ? (task.correct === 2 ? 'correct' : 'wrong') : ''}`}
            onClick={() => handleChoose(2)}
            disabled={chosen !== null}
          >
            {task.option2}
          </button>
        </div>
        {showFeedback && (
          <p className={`feedback ${correctChosen ? 'good' : 'bad'}`}>
            {correctChosen ? 'כל הכבוד! ✓' : 'לא הפעם. נסה שוב בשאלה הבאה.'}
          </p>
        )}
        {showFeedback && (
          isLast ? (
            <button className="next-btn" onClick={handleFinish}>סיום וחזרה לתפריט</button>
          ) : (
            <button className="next-btn" onClick={handleNext}>הבא →</button>
          )
        )}
      </div>
      {isLast && showFeedback && (
        <p className="summary"><strong>ניקוד: {score} מתוך {tasks.length}</strong></p>
      )}
    </>
  )
}

function YesNoGame({ tasks, onBack, title }) {
  const [index, setIndex] = useState(0)
  const [chosen, setChosen] = useState(null)
  const [score, setScore] = useState(0)
  const [showFeedback, setShowFeedback] = useState(false)
  const task = tasks[index]
  const isLast = index === tasks.length - 1
  const correctYes = task?.correct === true

  const handleChoose = (isYes) => {
    if (chosen !== null) return
    setChosen(isYes)
    if (isYes === correctYes) setScore((s) => s + 1)
    setShowFeedback(true)
  }

  const handleNext = () => {
    if (isLast) return
    setIndex((i) => i + 1)
    setChosen(null)
    setShowFeedback(false)
  }

  const handleFinish = () => {
    setIndex(0)
    setChosen(null)
    setShowFeedback(false)
    setScore(0)
    onBack()
  }

  if (!task) return null
  const correctChosen = (chosen === true && correctYes) || (chosen === false && !correctYes)

  return (
    <>
      <button className="back-btn" onClick={onBack}>← חזרה</button>
      <h2>{title || 'כן או לא?'}</h2>
      <p className="progress">שאלה {index + 1} מתוך {tasks.length}</p>
      <div className="task-card">
        <p className="phrase-display">{task.phrase}</p>
        <p className="instruction">האם זה הגיוני?</p>
        <div className="yesno-buttons">
          <button
            className={`option-btn ${chosen === true ? (correctYes ? 'correct' : 'wrong') : ''}`}
            onClick={() => handleChoose(true)}
            disabled={chosen !== null}
          >
            כן
          </button>
          <button
            className={`option-btn ${chosen === false ? (!correctYes ? 'correct' : 'wrong') : ''}`}
            onClick={() => handleChoose(false)}
            disabled={chosen !== null}
          >
            לא
          </button>
        </div>
        {showFeedback && (
          <p className={`feedback ${correctChosen ? 'good' : 'bad'}`}>
            {correctChosen ? 'כל הכבוד! ✓' : 'לא הפעם. התשובה: ' + (correctYes ? 'כן' : 'לא')}
          </p>
        )}
        {showFeedback && (
          isLast ? (
            <button className="next-btn" onClick={handleFinish}>סיום וחזרה לתפריט</button>
          ) : (
            <button className="next-btn" onClick={handleNext}>הבא →</button>
          )
        )}
      </div>
      {isLast && showFeedback && (
        <p className="summary"><strong>ניקוד: {score} מתוך {tasks.length}</strong></p>
      )}
    </>
  )
}

function VerbsGame({ tasks, onBack }) {
  const [index, setIndex] = useState(0)
  const [chosen, setChosen] = useState(null)
  const [score, setScore] = useState(0)
  const [showFeedback, setShowFeedback] = useState(false)
  const task = tasks[index]
  const isLast = index === tasks.length - 1
  const correctVerb = task?.subjectLabel === 'בנות' ? task?.verbFem : task?.verbMasc
  const options = task ? [task.verbFem, task.verbMasc].sort(() => Math.random() - 0.5) : []

  const handleChoose = (verb) => {
    if (chosen !== null) return
    setChosen(verb)
    if (verb === correctVerb) setScore((s) => s + 1)
    setShowFeedback(true)
  }

  const handleNext = () => {
    if (isLast) return
    setIndex((i) => i + 1)
    setChosen(null)
    setShowFeedback(false)
  }

  const handleFinish = () => {
    setIndex(0)
    setChosen(null)
    setShowFeedback(false)
    setScore(0)
    onBack()
  }

  if (!task) return null

  return (
    <>
      <button className="back-btn" onClick={onBack}>← חזרה</button>
      <h2>בחרו את הפועל המתאים</h2>
      <p className="progress">שאלה {index + 1} מתוך {tasks.length}</p>
      <div className="task-card">
        <p className="subject-display">{task.subject} _____</p>
        <div className="options">
          {options.map((verb) => {
            const showCorrect = chosen !== null && verb === correctVerb
            const showWrong = chosen !== null && chosen === verb && verb !== correctVerb
            const btnClass = showCorrect ? 'correct' : showWrong ? 'wrong' : ''
            return (
              <button
                key={verb}
                className={`option-btn ${btnClass}`}
                onClick={() => handleChoose(verb)}
                disabled={chosen !== null}
              >
                {verb}
              </button>
            )
          })}
        </div>
        {showFeedback && (
          <p className={`feedback ${chosen === correctVerb ? 'good' : 'bad'}`}>
            {chosen === correctVerb ? 'כל הכבוד! ✓' : 'לא הפעם. הנכון: ' + correctVerb}
          </p>
        )}
        {showFeedback && (
          isLast ? (
            <button className="next-btn" onClick={handleFinish}>סיום וחזרה לתפריט</button>
          ) : (
            <button className="next-btn" onClick={handleNext}>הבא →</button>
          )
        )}
      </div>
      {isLast && showFeedback && (
        <p className="summary"><strong>ניקוד: {score} מתוך {tasks.length}</strong></p>
      )}
    </>
  )
}

function SentenceCompletionGame({ tasks, onBack }) {
  const [index, setIndex] = useState(0)
  const [chosen, setChosen] = useState(null)
  const [score, setScore] = useState(0)
  const [showFeedback, setShowFeedback] = useState(false)
  const task = tasks[index]
  const isLast = index === tasks.length - 1
  const options = task ? [task.option1, task.option2].sort(() => Math.random() - 0.5) : []
  const correctWord = task ? (task.correct === 1 ? task.option1 : task.option2) : null

  const handleChoose = (word) => {
    if (chosen !== null) return
    setChosen(word)
    if (word === correctWord) setScore((s) => s + 1)
    setShowFeedback(true)
  }

  const handleNext = () => {
    if (isLast) return
    setIndex((i) => i + 1)
    setChosen(null)
    setShowFeedback(false)
  }

  const handleFinish = () => {
    setIndex(0)
    setChosen(null)
    setShowFeedback(false)
    setScore(0)
    onBack()
  }

  if (!task) return null
  const correctChosen = chosen === correctWord

  return (
    <>
      <button className="back-btn" onClick={onBack}>← חזרה</button>
      <h2>השלם את המשפט</h2>
      <p className="progress">שאלה {index + 1} מתוך {tasks.length}</p>
      <div className="task-card">
        <p className="sentence-display">{task.sentence}</p>
        <div className="options">
          {options.map((word) => {
            const showCorrect = chosen !== null && word === correctWord
            const showWrong = chosen !== null && chosen === word && word !== correctWord
            const btnClass = showCorrect ? 'correct' : showWrong ? 'wrong' : ''
            return (
              <button
                key={word}
                className={`option-btn ${btnClass}`}
                onClick={() => handleChoose(word)}
                disabled={chosen !== null}
              >
                {word}
              </button>
            )
          })}
        </div>
        {showFeedback && (
          <p className={`feedback ${correctChosen ? 'good' : 'bad'}`}>
            {correctChosen ? 'כל הכבוד! ✓' : 'לא הפעם. הנכון: ' + correctWord}
          </p>
        )}
        {showFeedback && (
          isLast ? (
            <button className="next-btn" onClick={handleFinish}>סיום וחזרה לתפריט</button>
          ) : (
            <button className="next-btn" onClick={handleNext}>הבא →</button>
          )
        )}
      </div>
      {isLast && showFeedback && (
        <p className="summary"><strong>ניקוד: {score} מתוך {tasks.length}</strong></p>
      )}
    </>
  )
}

function SentenceTransformGame({ tasks, onBack }) {
  const [index, setIndex] = useState(0)
  const [chosen, setChosen] = useState(null)
  const [score, setScore] = useState(0)
  const [showFeedback, setShowFeedback] = useState(false)
  const task = tasks[index]
  const isLast = index === tasks.length - 1
  const correctWord = task ? task.options[task.correct - 1] : null
  const options = task ? [...task.options].sort(() => Math.random() - 0.5) : []

  const handleChoose = (word) => {
    if (chosen !== null) return
    setChosen(word)
    if (word === correctWord) setScore((s) => s + 1)
    setShowFeedback(true)
  }

  const handleNext = () => {
    if (isLast) return
    setIndex((i) => i + 1)
    setChosen(null)
    setShowFeedback(false)
  }

  const handleFinish = () => {
    setIndex(0)
    setChosen(null)
    setShowFeedback(false)
    setScore(0)
    onBack()
  }

  if (!task) return null
  const correctChosen = chosen === correctWord

  return (
    <>
      <button className="back-btn" onClick={onBack}>← חזרה</button>
      <h2>קראו והשלימו – החלפת גוף</h2>
      <p className="progress">שאלה {index + 1} מתוך {tasks.length}</p>
      <div className="task-card">
        <p className="original-sentence">{task.original}</p>
        <p className="subject-display">{task.newSubject} _____</p>
        <div className="options">
          {options.map((word) => {
            const showCorrect = chosen !== null && word === correctWord
            const showWrong = chosen !== null && chosen === word && word !== correctWord
            const btnClass = showCorrect ? 'correct' : showWrong ? 'wrong' : ''
            return (
              <button
                key={word}
                className={`option-btn ${btnClass}`}
                onClick={() => handleChoose(word)}
                disabled={chosen !== null}
              >
                {word}
              </button>
            )
          })}
        </div>
        {showFeedback && (
          <p className={`feedback ${correctChosen ? 'good' : 'bad'}`}>
            {correctChosen ? 'כל הכבוד! ✓' : 'לא הפעם. הנכון: ' + correctWord}
          </p>
        )}
        {showFeedback && (
          isLast ? (
            <button className="next-btn" onClick={handleFinish}>סיום וחזרה לתפריט</button>
          ) : (
            <button className="next-btn" onClick={handleNext}>הבא →</button>
          )
        )}
      </div>
      {isLast && showFeedback && (
        <p className="summary"><strong>ניקוד: {score} מתוך {tasks.length}</strong></p>
      )}
    </>
  )
}

function RootTableGame({ tasks, onBack }) {
  const [index, setIndex] = useState(0)
  const [chosen, setChosen] = useState(null)
  const [score, setScore] = useState(0)
  const [showFeedback, setShowFeedback] = useState(false)
  const task = tasks[index]
  const isLast = index === tasks.length - 1
  const options = task ? [...task.options].sort(() => Math.random() - 0.5) : []

  const handleChoose = (word) => {
    if (chosen !== null) return
    setChosen(word)
    if (word === task.word) setScore((s) => s + 1)
    setShowFeedback(true)
  }

  const handleNext = () => {
    if (isLast) return
    setIndex((i) => i + 1)
    setChosen(null)
    setShowFeedback(false)
  }

  const handleFinish = () => {
    setIndex(0)
    setChosen(null)
    setShowFeedback(false)
    setScore(0)
    onBack()
  }

  if (!task) return null
  const correctChosen = chosen === task.word

  return (
    <>
      <button className="back-btn" onClick={onBack}>← חזרה</button>
      <h2>מילה מהשורש</h2>
      <p className="progress">שאלה {index + 1} מתוך {tasks.length}</p>
      <div className="task-card">
        <p className="phrase-display">הַשׁוֹרֶשׁ: {task.root}</p>
        <p className="instruction">מה הצורה ב־{task.ask}?</p>
        <div className="options">
          {options.map((word) => {
            const showCorrect = chosen !== null && word === task.word
            const showWrong = chosen !== null && chosen === word && word !== task.word
            const btnClass = showCorrect ? 'correct' : showWrong ? 'wrong' : ''
            return (
              <button
                key={word}
                className={`option-btn ${btnClass}`}
                onClick={() => handleChoose(word)}
                disabled={chosen !== null}
              >
                {word}
              </button>
            )
          })}
        </div>
        {showFeedback && (
          <p className={`feedback ${correctChosen ? 'good' : 'bad'}`}>
            {correctChosen ? 'כל הכבוד! ✓' : 'לא הפעם. הנכון: ' + task.word}
          </p>
        )}
        {showFeedback && (
          isLast ? (
            <button className="next-btn" onClick={handleFinish}>סיום וחזרה לתפריט</button>
          ) : (
            <button className="next-btn" onClick={handleNext}>הבא →</button>
          )
        )}
      </div>
      {isLast && showFeedback && (
        <p className="summary"><strong>ניקוד: {score} מתוך {tasks.length}</strong></p>
      )}
    </>
  )
}

const ENDPOINTS = [
  { key: 'logical', url: 'logical-sentences' },
  { key: 'logical5', url: 'logical-pairs-pg5' },
  { key: 'verbs', url: 'subject-verb-tasks' },
  { key: 'yesno3', url: 'yesno-phrases-pg3' },
  { key: 'yesno6', url: 'yesno-phrases-pg6' },
  { key: 'completion', url: 'sentence-completion' },
  { key: 'transform', url: 'sentence-transform' },
  { key: 'root', url: 'root-table' },
  { key: 'pyramid', url: 'pyramid' },
]

export default function App() {
  const [screen, setScreen] = useState('menu')
  const [pyramidLevel, setPyramidLevel] = useState(null)
  const [data, setData] = useState({})
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    let cancelled = false
    setLoading(true)
    setError(null)
    const urls = ENDPOINTS.map((e) => `${API_BASE}/${e.url}`)
    const FETCH_TIMEOUT_MS = 90000
    const fetchWithTimeout = (url) => {
      const controller = new AbortController()
      const timeoutId = setTimeout(() => controller.abort(), FETCH_TIMEOUT_MS)
      return fetch(url, { signal: controller.signal })
        .then((r) => {
          clearTimeout(timeoutId)
          return r.ok ? r.json() : Promise.reject(new Error(url))
        })
        .catch((err) => {
          clearTimeout(timeoutId)
          return Promise.reject(err)
        })
    }
    Promise.all(urls.map((url) => fetchWithTimeout(url)))
      .then((results) => {
        if (cancelled) return
        const next = {}
        ENDPOINTS.forEach((e, i) => { next[e.key] = results[i] })
        setData(next)
      })
      .catch(() => {
        if (!cancelled) setError('לא ניתן לטעון את המשימות. בדוק שהשרת רץ. (אם האתר על Render – חכה עד דקה עד שהשרת מתעורר.)')
      })
      .finally(() => {
        if (!cancelled) setLoading(false)
      })
    return () => { cancelled = true }
  }, [])

  if (loading) return <p className="loading">טוען...</p>
  if (error) return <p className="error-msg">{error}</p>

  if (screen === 'logical') {
    return <LogicalGame tasks={data.logical || []} onBack={() => setScreen('menu')} title="סמנו את המשפט ההגיוני" />
  }
  if (screen === 'logical5') {
    return <LogicalGame tasks={data.logical5 || []} onBack={() => setScreen('menu')} title="איזה משפט הגיוני?" />
  }
  if (screen === 'verbs') {
    return <VerbsGame tasks={data.verbs || []} onBack={() => setScreen('menu')} />
  }
  if (screen === 'yesno3') {
    return <YesNoGame tasks={data.yesno3 || []} onBack={() => setScreen('menu')} title="כן או לא? (צירוף-סגול)" />
  }
  if (screen === 'yesno6') {
    return <YesNoGame tasks={data.yesno6 || []} onBack={() => setScreen('menu')} title="כן או לא? (קמץ-פתח)" />
  }
  if (screen === 'completion') {
    return <SentenceCompletionGame tasks={data.completion || []} onBack={() => setScreen('menu')} />
  }
  if (screen === 'transform') {
    return <SentenceTransformGame tasks={data.transform || []} onBack={() => setScreen('menu')} />
  }
  if (screen === 'root') {
    return <RootTableGame tasks={data.root || []} onBack={() => setScreen('menu')} />
  }
  if (screen === 'pyramid') {
    if (!pyramidLevel) {
      return (
        <PyramidLevelMenu
          onChooseLevel={(lev) => setPyramidLevel(lev)}
          onBack={() => setScreen('menu')}
        />
      )
    }
    const pyramidTasks = (data.pyramid || []).filter((t) => t.level === pyramidLevel)
    const levelLabel = PYRAMID_LEVELS.find((l) => l.id === pyramidLevel)?.label || pyramidLevel
    return (
      <PyramidGame
        tasks={pyramidTasks}
        levelLabel={levelLabel}
        onBack={() => setPyramidLevel(null)}
      />
    )
  }
  return <Menu onChoose={setScreen} />
}
